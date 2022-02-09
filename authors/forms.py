from django import forms
from django.contrib.auth.models import User


def add_attr(field, attr_name, attr_new_value):
    existing_attr = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing_attr} {attr_new_value}'.strip()


def add_placeholder(field, attr_new_value):
    field.widget.attrs['placeholder'] = f'{attr_new_value}'.strip()


class RegisterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_attr(self.fields['username'], 'placeholder', 'Ex.: Doctor')
        add_attr(self.fields['last_name'], 'placeholder',
                 'Digite seu sobrenome aqui')
        add_attr(
            self.fields['email'], 'placeholder', 'Ex.: exemplo@exemplo.com.br'  # noqa: E501
        )

    password_2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Digite sua senha novamente'
        })
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
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
