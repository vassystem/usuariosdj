from django import forms

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
