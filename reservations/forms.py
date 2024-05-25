# forms.py
from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    date_of_journey = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = Reservation
        fields = ['train', 'class_type', 'from_place', 'to_place', 'date_of_journey']

class CancellationForm(forms.Form):
    pnr_number = forms.UUIDField()
 