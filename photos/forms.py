from django import forms
from .models import Image

class PhotosLetterForm(forms.Form):
    name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile']
        widgets = {
            'profile': forms.CheckboxSelectMultiple(),
        }