from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from .models import ShortLink


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # видаляємо поле підтвердження пароля
        del self.fields["password2"]

    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        # стандартні валідатори Django
        validate_password(password)
        return password


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]


class ShortLinkForm(forms.ModelForm):
    class Meta:
        model = ShortLink
        fields = ["original_url", "short_code"]
        labels = {
            "original_url": "Long link",
            "short_code": "Short name",
        }

    def clean_short_code(self):
        code = self.cleaned_data["short_code"]
        if ShortLink.objects.filter(short_code=code).exists():
            raise forms.ValidationError("This short code is already taken!")
        return code

