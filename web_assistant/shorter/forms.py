from django.forms import TextInput
from django.forms import ModelForm
from .models import Url

class UrlForm(ModelForm):
    class Meta:
        model = Url
        fields = ('source_url', )
        labels = {'source_url': 'Enter your long url'}
        widgets = {
            'source_url': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'example: https://github.com/ArturZhukovets?tab=repositories'
            })

        }
        error_messages = {'min_length': 'Your url is already too short! The new url will be longer'}