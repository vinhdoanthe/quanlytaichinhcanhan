from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from simple_history.models import HistoricalRecords


class Board(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    start_date = models.DateField()
    end_date = models.DateField()

    history = HistoricalRecords()


class Transaction(models.Model):

    INCOME = 'IN'
    EXPENSE = 'EX'

    TRANSACTION_TYPE_CHOICES = [
        (INCOME, _('Income')),
        (EXPENSE, _('Expense')),
    ]

    FIXED_EXPENSE = 'FE'
    VARIABLE_EXPENSE = 'VE'

    TRANSACTION_FIX_OR_VAR_CHOICES = [
        (FIXED_EXPENSE, _('Fixed Expense')),
        (VARIABLE_EXPENSE, _('Variable Expense')),
    ]

    ONE_TIME_TRANSACTION = 'OT'
    RECURRING_TRANSACTION = 'RT'

    TRANSACTION_DATE_TYPE_CHOICES = [
        (ONE_TIME_TRANSACTION, _('One Time Transaction')),
        (RECURRING_TRANSACTION, _('Recurring Transaction')),
    ]

    DAILY_RECURRING = 'DR'
    WEEKLY_RECURRING = 'WR'
    MONTHLY_RECURRING = 'MR'
    YEARLY_RECURRING = 'YR'

    TRANSACTION_RECURRING_TYPE_CHOICES = [
        (DAILY_RECURRING, _('Daily Recurring')),
        (WEEKLY_RECURRING, _('Weekly Recurring')),
        (MONTHLY_RECURRING, _('Monthly Recurring')),
        (YEARLY_RECURRING, _('Yearly Recurring')),
    ]

    PLAN_TRANSACTION = 'PT'
    ACTUAL_TRANSACTION = 'AT'

    TRANSACTION_PLAN_OR_ACTUAL_CHOICES = [
        (PLAN_TRANSACTION, _('Plan Transaction')),
        (ACTUAL_TRANSACTION, _('Actual Transaction')),
    ]

    amount = models.DecimalField(max_digits=20, decimal_places=2)
    transaction_type = models.CharField(max_length=2, choices=TRANSACTION_TYPE_CHOICES, default=EXPENSE)
    transaction_fix_or_var = models.CharField(
        max_length=2,
        choices=TRANSACTION_FIX_OR_VAR_CHOICES,
        default=VARIABLE_EXPENSE,
    )
    date_type = models.CharField(
        max_length=2,
        choices=TRANSACTION_DATE_TYPE_CHOICES,
        default=ONE_TIME_TRANSACTION,
    )
    recurring_type = models.CharField(
        max_length=2,
        choices=TRANSACTION_RECURRING_TYPE_CHOICES,
        default=MONTHLY_RECURRING,
    )
    transaction_date = models.DateField(default=timezone.now())
    recurring_start_date = models.DateField(null=True, blank=True)
    recurring_end_date = models.DateField(null=True, blank=True)
    plan_or_actual = models.CharField(
        max_length=2,
        choices=TRANSACTION_PLAN_OR_ACTUAL_CHOICES,
        default=ACTUAL_TRANSACTION,
    )
    description = models.TextField(max_length=500, null=True, blank=True)
    category = models.ForeignKey('TransactionCategory', null=True, blank=True, on_delete=models.CASCADE)

    board = models.ForeignKey('Board', on_delete=models.CASCADE)

    history = HistoricalRecords()


class TransactionCategory(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500, null=True, blank=True)

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    transaction_type = models.CharField(
        max_length=2,
        choices=Transaction.TRANSACTION_TYPE_CHOICES,
        default=Transaction.EXPENSE,
    )

    history = HistoricalRecords()

    def statistic_by_date_range(self, start_date, end_date):
        pass

    @classmethod
    def get_category_by_transaction_type(cls, transaction_type=Transaction.EXPENSE):
        return cls.objects.filter(transaction_type=transaction_type)
