from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="Username/Email", required=True, widget=forms.TextInput(attrs={
        "id": "username",
        "class": "username",
        "placeholder": "Enter your username or email"
    }))
    password = forms.CharField(max_length=100, label="Password", required=True, widget=forms.PasswordInput(attrs={
        "id": "password",
        "class": "password",
        "placeholder": "Enter the password"
    }))
    remember_me = forms.BooleanField(required=False, label="Remember me")


class RegistrationForm(forms.Form):
    fullname = forms.CharField(max_length=200, label="Full Name", required=True, widget=forms.TextInput(attrs={
        "id": "fullname",
        "class": "fullname",
        "placeholder": "Enter your full name"}
    ))
    username = forms.CharField(max_length=100, label="Username/Email", required=True, widget=forms.TextInput(attrs={
        "id": "username",
        "class": "username",
        "placeholder": "Enter your username or email"
    }))
    password = forms.CharField(max_length=100, label="Password", required=True, widget=forms.PasswordInput(attrs={
        "id": "password",
        "class": "password",
        "placeholder": "Enter the password"
    }))
    re_password = forms.CharField(max_length=100, label="Password", required=True, widget=forms.PasswordInput(attrs={
        "id": "re-password",
        "class": "re-password",
        "placeholder": "Re-Enter the password"
    }))
    email = forms.EmailField(min_length=10, label="Email", required=True, widget=forms.EmailInput(attrs={
        "id": "email",
        "class": "email",
        "placeholder": "Enter your mail address"
    }))
