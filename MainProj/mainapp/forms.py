from django import forms
from .models import TelegrafModel
import re
import gettext ; _ = gettext.gettext
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe


class MainForm(forms.ModelForm):
    uri = forms.CharField(label=False, max_length=6, widget=forms.TextInput(
        attrs={'class': 'form-control', 'autocomplete': 'off', 'placeholder': 'desired link'}))
    content = forms.CharField(label=False, widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Your text (HTML tags allowed) ...'}))
    file = forms.FileField(label=False, widget=forms.FileInput(
        attrs={'class': 'form-control', 'multiple': True}), required=False)

    class Meta:
        model = TelegrafModel
        fields = ['uri', 'content', 'file']
        # widgets = {
        #     'uri': forms.TextInput(attrs= {'class': 'form-control', 'autocomplete': 'off', 'placeholder': 'desired URI'}),
        #     'content': forms.Textarea(attrs= {'class': 'form-control', 'rows': 5, 'placeholder': 'Your text...'}),
        #     'file': forms.FileInput(attrs= {'class': 'form-control'}),
        # }

    # uri field validation - must match any "word" character (letter, digit or underscore)
    def clean_uri(self):
        uri = self.cleaned_data['uri']
        if not re.fullmatch(r'\w+', uri):
            raise ValidationError(_(mark_safe('Link may contain only letters, digits or underscores.<br>Case-sensitive. Max. 6 characters.')), code='invalid')
        return uri
