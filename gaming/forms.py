from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import usernames
from django import forms

# It creates a form for the user to fill out.
class SignUpForm(UserCreationForm):
    
    # Adding an email field to the form.
    email = forms.EmailField(required=True)

    # A class that is used to create a form.
    class Meta:
        # Creating a form for the user to fill out.
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

    def save(self, commit=True):
        """
        The save() method of the form saves the data to the database
        
        :param commit: If True, then the changes to the object are saved to the database. If False, then
        the changes are not saved, defaults to True (optional)
        :return: The user object.
        """
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

# This class is a form that allows the user to add a game and username to the database.
class addForm(forms.ModelForm):

    # The Meta class is a class within the class that defines the model and fields that will be used
    # in the form.
    class Meta:
        # Creating a form for the user to fill out.
        model = usernames
        fields = ('game', 'username')
