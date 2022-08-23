from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import Profile

User = get_user_model()


class MyUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name')

    def is_valid(self):
        super().is_valid()
        data = self.cleaned_data
        if not data.get('first_name'):
            self.add_error('first_name', 'First Name fields must be filled')
            return False
        return True


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
        labels = {'first_name': 'Name', 'last_name': 'Last Name'}


class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'about_user', 'git']


class PasswordChangeForm(forms.ModelForm):
    password = forms.CharField(label="New password", strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Confirm password", widget=forms.PasswordInput, strip=False)
    old_password = forms.CharField(label="Old password", strip=False, widget=forms.PasswordInput)

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Passwords do not match!')
        return password_confirm

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.instance.check_password(old_password):
            raise forms.ValidationError('The old password is wrong!')
        return old_password

    def save(self, commit=True):
        user = self.instance
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['password', 'password_confirm', 'old_password']
