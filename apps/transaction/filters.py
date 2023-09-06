from apps.transaction.forms import TransactionForm
from apps.transaction.models import Transaction
from django_filters import (
    DateFromToRangeFilter,
    FilterSet,
)
from django_filters.widgets import DateRangeWidget


class TransactionFilter(FilterSet):
    transaction_date = DateFromToRangeFilter(
        widget=DateRangeWidget(attrs={'placeholder': 'YYYY-MM-DD'}),
    )

    class Meta:
        model = Transaction
        fields = [
            'transaction_type',
            'date_type',
            'transaction_date',
            'category',
            'transaction_fix_or_var',
            'amount',
        ]
