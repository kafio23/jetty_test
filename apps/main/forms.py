from django import forms


class LoginForm(forms.Form):

    email = forms.EmailField(required=True,  widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Correo electrónico', 'autofocus': 'autofocus'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
