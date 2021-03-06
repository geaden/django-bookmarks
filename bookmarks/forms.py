import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from django.utils.translation import gettext_lazy as _

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    verify = forms.CharField(label='Password (Again)', widget=forms.PasswordInput())
    
    def clean_verify(self):
       if 'password' in self.cleaned_data:
           password = self.cleaned_data['password']
           verify = self.cleaned_data['verify']
           if password == verify:
               return verify
           raise forms.ValidationError('Passwords do not match.')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Username can only contain alphanumeric characters and the underscore.')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Username is already taken.')


class BookmarkSaveForm(forms.Form):
    url = forms.URLField(label='URL',
                         widget=forms.TextInput(attrs={'size': 64}))
    title = forms.CharField(label='Title',
                            widget=forms.TextInput(attrs={'size': 64}))
    tags = forms.CharField(label='Tags',
                           required=False,
                           widget=forms.TextInput(attrs={'size': 64}))
    share = forms.BooleanField(label='Share on the main page',
                               required=False)
  

class SearchForm(forms.Form):
    query = forms.CharField(label='Enter a keyword to search for',
                            widget=forms.TextInput(attrs={'size': 32})   
                           )


class FriendInvitationForm(forms.Form):
  name = forms.CharField(label=_('Friend\'s Name'), localize=True)
  email = forms.EmailField(label=_('Friend\'s Email'), localize=True)

