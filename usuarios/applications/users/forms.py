from django import forms
from django.contrib.auth import authenticate
from .models import User

class UserRegisterForm(forms.ModelForm):
    """Form definition for UserRegister."""
    
    password1 = forms.CharField(
        label='contrasena',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contrasena'
            }             
        )
    )

    password2 = forms.CharField(
        label='contrasena',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir Contrasena'
            }
        )
    )

    class Meta:
        """Meta definition for UserRegisterform."""

        model = User
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
            'genero'
            )

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contrasenas no coinciden')


class LoginForm(forms.Form):

    username = forms.CharField(
        label='contrasena',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'username',
                'style': '{ margin: 10px }'
            }
        )
    )

    password = forms.CharField(
        label='contrasena',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Ingrese Contrasena'
            }
        )
    )
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Los datos de usuario no son correctos')

        return self.cleaned_data


class UpdatePasswordForm(forms.Form):
    password1 = forms.CharField(
        label='contrasena',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Actual'
            }
        )
    )

    password2 = forms.CharField(
        label='contrasena',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Nueva'
            }
        )
    )

class VerificacionForm(forms.Form):
    codregistro = forms.CharField(required=True)    
