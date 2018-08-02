from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label='用户名',
        error_messages={
            'required': '用户名不能为空',
        },
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '用户名',
            }
        )
    )

    password = forms.CharField(
        label='密码',
        error_messages={
            'required': '密码不能为空',
        },
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '密码',
            }
        )
    )

