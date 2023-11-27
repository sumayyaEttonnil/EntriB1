
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import CustomUser, Stop


class UserRegistration(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRegistration, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''  # Clear the help text for the 'username' field

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']
        labels = {
            'username': 'Username',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'id_email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_phone_number'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'id_password1'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'id_password2'}),
        }


from django import forms


class BusStopSelectionForm(forms.Form):
    source = forms.ModelChoiceField(label='Source',  queryset=Stop.objects.all())
    destination = forms.ModelChoiceField(label='Destination',  queryset=Stop.objects.all())
    date = forms.DateField(label='Date', widget=forms.DateInput(attrs={'type': 'date'}))
