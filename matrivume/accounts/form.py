from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class RegistrationForm(forms.ModelForm):

	password1 = forms.CharField(max_length=32, min_length=4, widget=forms.PasswordInput)
	password2 = forms.CharField(max_length=32, min_length=4, widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'password1', 'password2', 'email')
