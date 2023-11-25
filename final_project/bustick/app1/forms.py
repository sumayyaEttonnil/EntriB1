
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class UserRegistration(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']



from django import forms


class BusStopSelectionForm(forms.Form):
    source = forms.CharField(label='Source', max_length=100)
    destination = forms.CharField(label='Destination', max_length=100)
    date = forms.DateField(label='Date', widget=forms.DateInput(attrs={'type': 'date'}))
