from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import usernames
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class addForm(forms.ModelForm):

    class Meta:
        model = usernames
        fields = ('game', 'username')
