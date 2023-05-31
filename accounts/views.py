from django.shortcuts import redirect,render

from django.contrib import messages,auth

from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required

from clicommands.models import Command
from django.contrib.auth.models import User
from catalogue.models import Catalogue
from opmode.models import Opmode

from django.views.generic import CreateView, TemplateView, RedirectView


from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str # force_text on older versions of Django

from .forms import SignUpForm, token_generator, user_model, EditProfileInfoForm, CustomChangingPassword

#from .models import Profile

# Create your views here.
####################################################################
class SignUpView(CreateView):

    form_class = SignUpForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('check_email')

    def form_valid(self, form):
        to_return = super().form_valid(form) #"""If the form is valid, redirect to the supplied URL."""
        user = form.save()
        user.is_active = False  # Turns the user status to inactive
        user.save()
        form.send_activation_email(self.request, user)
        return to_return

class ActivateView(RedirectView):
    url = reverse_lazy('success')

    # Custom get method
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = user_model.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, user_model.DoesNotExist):
            user = None

        if user is not None and token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            auth.login(request, user)
            return super().get(request, uidb64, token)
        else:
            return render(request, 'accounts/activate_account_invalid.html')

class CheckEmailView(TemplateView):
    template_name = 'accounts/check_email.html'

class SuccessView(TemplateView):
    template_name = 'accounts/success.html'

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']


        user = auth.authenticate(username=username, password=password)


        if user is not None:

            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You are logged out")
        return redirect('index')

def dashboard(request):
    if request.user.is_authenticated:
        user_id = request.user.id

        catalogues = Catalogue.objects.all().order_by('category__name', 'title').filter(is_published=True)
        user_cmds = Command.objects.all().order_by('cmd_date').filter(owner_id=user_id)
        opmodes = Opmode.objects.all().order_by('name')

        context = {
            'user_commands': user_cmds,
            'catalogues': catalogues,
            'opmodes':opmodes,
        }
        return render(request, 'accounts/dashboard.html',context)
    else:
        return redirect('login')
@login_required
def profile(request, user_id=0):
    if not user_id:
        profile = request.user.profile
    else:
        user = user_model.objects.get(pk=user_id)
        profile =  user.profile

    context = {
        'profile':profile
    }
    return render(request,'accounts/profile.html',context)

@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method != "POST":
        Profileform = EditProfileInfoForm(instance=profile)
        context = {
            'avatar': profile.avatar,
            'profile': profile,
            'form': Profileform
        }
        return render(request, 'accounts/updateprofile.html', context)
    else:

        Profileform = EditProfileInfoForm(request.POST,instance=profile)
        if Profileform.is_valid():
            Profileform.save()
        return redirect('edit_profile')

@login_required
def delete_profile(request,user_id):
    if request.method == "POST":
        user = User.objects.all().filter(pk=user_id)
        user.delete()
    return redirect('index')

@login_required
def contributors(request):
    User = auth.get_user_model()
    UsersList = User.objects.all().order_by('username')
    users_cmds = Command.objects.all().order_by('cmd_date')

    profile_to_public = []

    for user in UsersList:
        if user.profile.Published == False:
            continue
        for command in users_cmds:
            if str(command.owner) == str(user.profile):
                profile_to_public.append(user.profile)

    context = {
        'profiles': list(dict.fromkeys(profile_to_public)) # remove doulicates from the list by converting into dict
    }

    return render(request, 'pages/contributors.html',context)

class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomChangingPassword
    template_name = 'change-password.html'
    def form_valid(self, form):
        messages.success(self.request, 'Your password has been changed.')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, 'Your password has NOT been changed.')
        return super().form_invalid(form)

class CustomPasswordResetView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('login')