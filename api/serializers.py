from rest_framework import serializers

from .models import Product
from django import forms

from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User 



class ProductSerializer(serializers.ModelSerializer):
     class Meta:
        model = Product
        fields = '__all__'
        
        
class DataSerializer(forms.ModelForm):
     class Meta:
        model = Product
        #fields = '__all__'
        fields = ('name', 'author', 'category', 'price', 'description', 'stars')

        widgets = {
		           'name': forms.TextInput(attrs={'class': 'form-control'}),
                 'author': forms.Select(attrs={'class': 'form-control'}),
		           'category': forms.TextInput(attrs={'class': 'form-control'}),
		           'price': forms.TextInput(attrs={'class': 'form-control'}),
		           'description': forms.Textarea(attrs={'class': 'form-control'}),
		           'stars': forms.TextInput(attrs={'class': 'form-control'}),

                 }



