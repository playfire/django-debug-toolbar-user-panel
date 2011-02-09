from django.contrib.auth.models import User

from django import forms

class UserForm(forms.Form):
    val = forms.CharField(label='User.{id,username,email}')

    def get_lookup(self):
        val = self.cleaned_data['val']

        if '@' in val:
            return {'email': val}

        try:
            return {'pk': int(val)}
        except:
            return {'username': val}
