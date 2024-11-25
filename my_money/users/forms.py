from django import forms

class LoginForm(forms.Form):
    """
    Форма для входа пользователя.

    Поля:
    - email: Адрес электронной почты пользователя.
    - password: Пароль пользователя (отображается как текст).
    """
    email = forms.EmailField(label='Email', max_length=50)
    password = forms.CharField(label='Пароль', widget=forms.TextInput)

