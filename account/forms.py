from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

from account.models import CustomUser


class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    user_email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))

    mobile_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Mobile Number'}))
    postcode = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Postcode'}))
    country = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Country'}))
    town = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Town'}))
    street_and_house = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Street and House'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))


    class Meta:
        model = CustomUser
        fields = ('username', 'user_email', 'first_name', 'last_name', 'mobile_number', 'postcode', 'country', 'town', 'street_and_house', 'password1',
                  'password2')

class UserUpdateForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        required=False,
        help_text="Leave blank if you don't want to change your password.",
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'user_email', 'first_name', 'last_name', 'mobile_number', 'postcode', 'country', 'town', 'street_and_house', 'password')
    def clean_password(self):
        password = self.cleaned_data.get("password")
        if password:
            return password
        return None

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password")
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
