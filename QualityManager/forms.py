from django import forms
class Reg(forms.Form):
    username=forms.CharField(
        required=True,
        max_length=16,
        min_length=2,
        error_messages={
            'required':'用户名不能为空',
            'max_length':'最大长度不得超过16位',
            'min_length':'最小长度不得少于2位'
        },
        label='用户名',
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'请输入用户名'})
                             )
    pwd=forms.CharField(
        required=True,
        max_length=16,
        min_length=2,
        error_messages={
            'required': '用户名不能为空',
            'max_length': '最大长度不得超过16位',
            'min_length': '最小长度不得少于2位'
        },
        label='密码',
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'请输入密码','type':'password'})
    )
    email=forms.EmailField(
        required=True,
        max_length=32,
        min_length=2,
        error_messages={
            'required': '用户名不能为空',
            'max_length': '最大长度不得超过32位',
            'min_length': '最小长度不得少于2位',
            'invalid':'邮箱格式错误'
        },
        widget=forms.EmailInput(attrs={{'class':'form-control','placeholder':'请输入邮箱'}})
    )