from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label='Your username', max_length=100)
    firstname = forms.CharField(label='Your name', max_length=100)
    lastname = forms.CharField(label='Your lastname', max_length=100)
    adress = forms.CharField(label='Your adress', max_length=100)
    city = forms.CharField(label='Your city', max_length=100)
    state = forms.CharField(label='Your state', max_length=100)
    email = forms.CharField(label='Your email', max_length=100)
    phone = forms.IntegerField(label='Your phone')
    password = forms.CharField(label='Your psw')
