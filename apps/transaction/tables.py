from django.utils.translation import gettext_lazy as _

from apps.transaction.models import (
    Board,
    Transaction,
)
from django_tables2 import (
    columns,
    tables,
)
from django_tables2.utils import A


class BoardTable(tables.Table):
    detail_link = columns.LinkColumn(
        'board_detail',
        args=[A('pk')],
        text=_('Detail'),
    )

    class Meta:
        model = Board
        template_name = 'django_tables2/bootstrap5.html'
        fields = ('name', 'description', 'start_date', 'end_date', 'detail_link')


class TransactionTable(tables.Table):

    class Meta:
        model = Transaction
        template_name = 'django_tables2/bootstrap5.html'
        fields = (
            'name', 'description', 'amount', 'transaction_type', 'transaction_fix_or_var',
            'transaction_date_type', 'transaction_recurring_type', 'transaction_plan_or_actual',
            'transaction_date',
        )
        exclude = ('board',)
