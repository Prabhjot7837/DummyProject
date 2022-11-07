from dataclasses import fields
from django import forms
from .models import Product

class productForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'rollno': forms.TextInput(attrs={'class':'form-control'}),
            'designation': forms.TextInput(attrs={'class':'form-control'}),
        }