from rest_framework import serializers

from .models import Product
from django import forms


class ProductSerializer(serializers.ModelSerializer):
     class Meta:
        model = Product
        fields = '__all__'
        
        
class DataSerializer(forms.ModelForm):
     class Meta:
        model = Product
        #fields = '__all__'
        fields = ('name', 'category', 'price', 'description', 'stars')

        widgets = {
		           'name': forms.TextInput(attrs={'class': 'form-control'}),
		           'category': forms.TextInput(attrs={'class': 'form-control'}),
		           'price': forms.TextInput(attrs={'class': 'form-control'}),
		           'description': forms.Textarea(attrs={'class': 'form-control'}),
		           'stars': forms.TextInput(attrs={'class': 'form-control'}),

                 }