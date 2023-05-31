from django.forms import ModelForm,HiddenInput

from .models import Command

class DefineCommandForm(ModelForm):
    class Meta:
        model = Command
        fields = '__all__'
        exclude = ['owner']
        widgets = {
            'owner':HiddenInput(),
            'cmd_date':HiddenInput(),
            'is_published':HiddenInput(),
        }