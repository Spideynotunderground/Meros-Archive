from django import forms
from .models import Ambassador


class AmbassadorForm(forms.ModelForm):
    class Meta:
        model = Ambassador
        fields = ('full_name', 'email', 'phone_number', 'tg_username')
