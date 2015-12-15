from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label='Your username', max_length=100)
    firstname = forms.CharField(label='Your name', max_length=100)
    lastname = forms.CharField(label='Your lastname', max_length=100)
    email = forms.CharField(label='Your email', max_length=100)
    phone = forms.IntegerField(label='Your phone')
    password = forms.CharField(label='Your psw')



class LoginForm(forms.Form):
    username = forms.CharField(label='Your username', max_length=100)
    password = forms.CharField(label='Your password', widget=forms.PasswordInput)

class PaymentForm(forms.Form):
    payment_type = forms.CharField(label='Your payment_type', max_length=100)
    please_select = forms.CharField(label='Your payment_type', max_length=100)
    Address = forms.CharField(label='Your payment_type', max_length=100)
    promotion_code = forms.CharField(label='Your payment_type', max_length=100)
    comment  = forms.CharField(label='Your payment_type', max_length=1000)
