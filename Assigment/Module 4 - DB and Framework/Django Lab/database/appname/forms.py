from django import forms
from .models import StudInfo

class StudInfoForm(forms.ModelForm):
    class Meta:
        model = StudInfo
        fields = "__all__"
