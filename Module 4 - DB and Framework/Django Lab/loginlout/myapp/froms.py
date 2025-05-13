from django import forms
from .models import sinup


class sinup(forms.ModelForm):
    class Meta:
        model = sinup
        fields = "__all__"
