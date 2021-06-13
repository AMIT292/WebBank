from django.core import validators
from django import forms
from django.forms import widgets
from .models import *

class updation_new(forms.ModelForm):
    class Meta:
        model=Transfer
        fields=['acc_no_of_reciever ','amount_transferred' ]
        