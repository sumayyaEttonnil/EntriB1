from django import forms
from app1.models import Bus, BoardingStop, DestinationStop
from django.forms.models import inlineformset_factory

class BusForm1(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ['name', 'total_seats', 'available_seats', 'bus_type']

BoardingStopFormSet = inlineformset_factory(Bus, BoardingStop, fields=('stop', 'departure_time', 'distance'), extra=3)
DestinationStopFormSet = inlineformset_factory(Bus, DestinationStop, fields=('stop', 'arrival_time', 'distance'), extra=3)


class BusDateForm(forms.Form):
    # Fetching bus names from Bus model
    bus_name = forms.ChoiceField(
        choices=[(bus.name, bus.name) for bus in Bus.objects.all()],
        label='Bus Name'
    )
    date = forms.DateField(label='Date', widget=forms.DateInput(attrs={'type': 'date'}))

from app1.models import Stop
class StopForm(forms.ModelForm):
    class Meta:
      model=Stop
      fields=['name']
