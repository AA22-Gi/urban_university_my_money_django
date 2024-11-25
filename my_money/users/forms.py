from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=50)
    password = forms.CharField(label='Пароль', widget=forms.TextInput)