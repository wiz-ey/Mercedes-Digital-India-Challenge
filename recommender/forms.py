from django import forms
from .models import New
class CxForm(forms.ModelForm):
    class Meta:
        model = New
        fields = '__all__'
