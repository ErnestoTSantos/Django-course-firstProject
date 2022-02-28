import re

from django import forms
from django.contrib.auth.models import User
from django.forms import ValidationError


def add_attr(field, attr_name, attr_new_value):
    # Função para adicionar coisas aos campos
    existing_attr = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing_attr} {attr_new_value}'.strip()


def add_placeholder(field, attr_new_value):
    add_attr(field, 'placeholder', attr_new_value)


def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError((
            'Password must have at least one uppercase letter, '
            'one lowecase letter and onde number. The lenght should be '
            'at least 8 characters.'
        ),
            code='Invalid'
        )


class RegisterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Ex.: Doctor')
        add_placeholder(self.fields['last_name'], 'Digite seu sobrenome aqui')
        add_attr(
            self.fields['email'], 'placeholder', 'Ex.: exemplo@exemplo.com.br'  # noqa: E501
        )
        # add_attr(self.fields['username'], 'css', 'a-css-class')

    password_2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Your password'
        }),
        error_messages={
            'required': 'Password must not be empty'
        },
        help_text={
            'Password must have at least one uppercase letter, '
            'one lowecase letter and onde number. The lenght should be '
            'at least 8 characters.'
        },
        validators=[strong_password, ]
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'password_2'
        ]
        labels = {
            'first_name': 'Primeiro nome',
            'last_name': 'Sobre nome',
            'username': 'Nome de usuário',
            'email': 'E-mail',
            'password': 'Senha',
        }
        help_texts = {
            'email': 'O e-mail precisa ser válido'
        }
        error_messages = {
            'username': {
                'require': 'Esse campo não pode ficar vazio',
            },
            'password': {
                'require': 'Este campo não pode ficar vazio'
            }
        }
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Digite seu primeiro nome aqui',
                # Posso colocar classes nos elementos por aqui também
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Digite uma senha aqui'
            })
        }
    """
    Forma de fazer validação por campo específico, sendo apenas do User

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if 6 > len(password):
            raise ValidationError(
                'A senha precisa ter no mínimo 6 caracteres!'
            )

        return password
    """

    def clean_first_name(self):
        data = self.cleaned_data.get('first_name')

        if 3 > len(data):
            raise ValidationError(
                'O nome precisa ter no mínimo 3 caracteres!'
            )

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password_2 = cleaned_data.get('password_2')

        print(cleaned_data)

        if 6 > len(password):
            raise ValidationError(
                'A senha precisa ter no mínimo 6 caracteres!'
            )

        if password != password_2:
            password_confirmation_error = ValidationError(
                'As senhas precisam ser iguais!',
                code='invalid'
            )
            raise ValidationError({
                'password': password_confirmation_error,
                'password_2': [password_confirmation_error]
            })
