from django import forms
from .models import *

class productForm(forms.ModelForm):
    class Meta:
        model=product_detail
        fields=['pname','qty','price','pimage']