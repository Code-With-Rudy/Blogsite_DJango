# blog/forms.py
from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm # Import Django's built-in form
from django.contrib.auth.models import User # Import the User model

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content'] # Fields user can edit

# New User Registration Form
class UserRegisterForm(UserCreationForm):
    # You can add more fields here if you want to extend the default User model
    # For example, to add an email field to the registration form:
    email = forms.EmailField() # Add this line if you want to collect email during registration

    class Meta(UserCreationForm.Meta):
        model = User
        # Define the fields to be included in the registration form.
        # 'username' and 'password' (password1, password2) are included by default from UserCreationForm.Meta.fields
        fields = UserCreationForm.Meta.fields + ('email',) # Add 'email' if you added the field above.
        # If you don't add the email field in the form, just use:
        # fields = UserCreationForm.Meta.fields