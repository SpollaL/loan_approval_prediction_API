from django import forms
from .models import Approval

class PredictionForm(forms.ModelForm):
    class Meta:
        model = Approval
        fields = '__all__'
