from django import forms
from .models import Submission

class UserSubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['image', 'day', 'part', 'code']
        widgets = {
            'day': forms.Select(attrs={'class': 'form-control'}),
            'part': forms.Select(attrs={'class': 'form-control'}),
        }
