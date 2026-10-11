from django import forms
from .models import CustomUser


class UserRegistrationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=CustomUser
        fields=['username','email','password']

    def clean(self):
        clean_data=super().clean()
        password=clean_data.get("password")
        confirm_password=clean_data.get("confirm_password")
        if password!=confirm_password:
            raise forms.ValidationError("password dont match")
        return clean_data
    


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserPassworchangeForm(forms.Form):
    old_password=forms.CharField(widget=forms.PasswordInput)
    new_password=forms.CharField(widget=forms.PasswordInput)
    conf_password=forms.CharField(widget=forms.PasswordInput)


