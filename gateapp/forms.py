from django import forms
from .models import Visitor


class VisitorForm(forms.ModelForm):

    class Meta:
        model = Visitor

        fields = [
            'visitor_name',
            'phone',
            'company',
            'purpose',
            'person_to_meet',
            'vehicle_number',
        ]

        widgets = {
            'visitor_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter visitor name'
            }),

            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number'
            }),

            'company': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter company name'
            }),

            'purpose': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter purpose of visit'
            }),

            'person_to_meet': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter person to meet'
            }),

            'vehicle_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter vehicle number'
            }),
        }