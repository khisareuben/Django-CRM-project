from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Record

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already in use.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match.")

        return cleaned_data


class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, label="First Name", widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5 w-[600px] mb-[10px]'}))
    
    last_name = forms.CharField(required=True, label="Last Name", widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5 w-[600px] mb-[10px]'}))
    
    email = forms.EmailField(required=True, label="Email", widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5 w-[600px] mb-[10px]'}))
    
    phone = forms.CharField(required=True, label="Phone", widget=forms.TextInput(attrs={'placeholder': 'Phone', 'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5 w-[600px] mb-[10px]'}))
    
    address = forms.CharField(required=True, label="Address", widget=forms.TextInput(attrs={'placeholder': 'Address', 'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5 w-[600px] mb-[10px]'}))
    
    city = forms.CharField(required=True, label="City", widget=forms.TextInput(attrs={'placeholder': 'City', 'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5 w-[600px] mb-[10px]'}))
    
    state = forms.CharField(required=True, label="State", widget=forms.TextInput(attrs={'placeholder': 'State', 'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5 w-[600px] mb-[10px]'}))
    
    zipcode = forms.CharField(required=True, label="Zipcode", widget=forms.TextInput(attrs={'placeholder': 'Zipcode', 'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5 w-[600px] mb-[10px]'}))
    
    class Meta:
      model = Record
      exclude = ('user',)
      