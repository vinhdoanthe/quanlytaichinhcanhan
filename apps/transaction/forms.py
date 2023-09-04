from django import forms

from apps.transaction.models import Board


class BoardForm(forms.ModelForm):

    class Meta:
        model = Board
        fields = ('name', 'description', 'start_date', 'end_date')
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
