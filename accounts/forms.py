from django import forms
from django.forms import ModelForm
# from captcha.fields import CaptchaField

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from django.template.loader import render_to_string

from .token import token_generator

from .models import Profile


user_model = get_user_model()
#
# class CaptchaTestForm(forms.Form):
#     captcha = CaptchaField()

class SignUpForm(UserCreationForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('That email is being used')
        return email

    email = forms.EmailField(
        max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = user_model
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
        # We need the user object, so it's an additional parameter

    def send_activation_email(self, request, user):
        current_site = get_current_site(request)
        subject = 'Activate Your Account'
        message = render_to_string(
            'accounts/activate_account.html',
            {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': token_generator.make_token(user),
            }
        )
        user.email_user(subject, message, html_message=message)
class EditProfileInfoForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user','avatar'] #avatar cannot be uploaded

class CustomChangingPassword(PasswordChangeForm):

    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'type':'password'}),label='Old Password')
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'type':'password'}),label='New Password')
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'type':'password'}),label='Retype Password')
    class Meta:
        model = User
        fields = [
            'old_password',
            'new_password1',
            'new_password2',
        ]
