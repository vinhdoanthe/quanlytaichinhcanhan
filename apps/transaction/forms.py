from django import forms

from apps.transaction.models import (
    Board,
    Transaction,
    TransactionCategory,
)
from crispy_forms.helper import (
    FormHelper,
    Layout,
)


class BoardForm(forms.ModelForm):

    class Meta:
        model = Board
        fields = ('name', 'description', 'start_date', 'end_date')
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = (
            'amount', 'transaction_type', 'transaction_fix_or_var',
            'date_type', 'recurring_type', 'transaction_date',
            'recurring_start_date', 'recurring_end_date', 'plan_or_actual',
            'description', 'category',
        )
        widgets = {
            'amount': forms.NumberInput(attrs={'step': '1000'}),
            'transaction_date': forms.DateInput(attrs={'type': 'date'}),
            'recurring_start_date': forms.DateInput(attrs={'type': 'date'}),
            'recurring_end_date': forms.DateInput(attrs={'type': 'date'}),
        }
        localized_fields = ('amount',)


class DailyTransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = (
            'amount',
            'transaction_type',
            'transaction_fix_or_var',
            'transaction_date',
            'description',
            'category',
        )
        widgets = {
            'amount': forms.NumberInput(attrs={'step': '1000'}),
            'transaction_date': forms.DateInput(attrs={'type': 'date'}),
        }
        localized_fields = ('amount',)


class CategoryForm(forms.ModelForm):

    class Meta:
        model = TransactionCategory
        fields = ('name', 'description', 'transaction_type')


DailyTransactionFormSet = forms.formset_factory(
    form=DailyTransactionForm,
    can_delete=True,
)


class DailyTransactionFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(DailyTransactionFormHelper, self).__init__(*args, **kwargs)
        self.layout = Layout(
            'amount',
            'transaction_type',
            'transaction_fix_or_var',
            'transaction_date',
            'description',
            'category',
        )
        self.template = 'bootstrap5/table_inline_formset.html'
