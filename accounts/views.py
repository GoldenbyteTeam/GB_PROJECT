from django.shortcuts import redirect,render
from django.contrib import messages,auth
from django.contrib.auth.models import User
from clicommands.models import Command
from catalogue.models import Catalogue
from opmode.models import Opmode

from django.views.generic import CreateView, TemplateView, RedirectView

from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str # force_text on older versions of Django

from .forms import SignUpForm, token_generator, user_model

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



