from django import forms
from .models import *

class usersignupform(forms.ModelForm):
    class Meta:
        model = usersignup  
        fields = "__all__"

        