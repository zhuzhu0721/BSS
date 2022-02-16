from django import forms
from captcha.fields import CaptchaField
from django.core import validators


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码',error_messages={"invalid":"验证码错误"})
class RegisterForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label="手机号码", max_length=11,validators=[validators.RegexValidator("1[3456789]\d{9}", message='请输入正确格式的手机号码！')],widget=forms.TextInput(attrs={'class': 'form-control'}))
    lan_name = forms.CharField(label="所属部门", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码')