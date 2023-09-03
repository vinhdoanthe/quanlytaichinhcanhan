from django.db import models
from django.utils.translation import gettext_lazy as _

from simple_history.models import HistoricalRecords


class Board(models.Model):

        name = models.CharField(max_length=100)
        description = models.CharField(max_length=100)

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
    transaction_fix_or_var = models.CharField(max_length=2, choices=TRANSACTION_FIX_OR_VAR_CHOICES, default=VARIABLE_EXPENSE)
    date_type = models.CharField(max_length=2, choices=TRANSACTION_DATE_TYPE_CHOICES, default=ONE_TIME_TRANSACTION)
    recurring_type = models.CharField(max_length=2, choices=TRANSACTION_RECURRING_TYPE_CHOICES, default=MONTHLY_RECURRING)
    transaction_date = models.DateField(auto_now_add=True)
    recurring_start_date = models.DateField()
    recurring_end_date = models.DateField()
    plan_or_actual = models.CharField(max_length=2, choices=TRANSACTION_PLAN_OR_ACTUAL_CHOICES, default=ACTUAL_TRANSACTION)
    description = models.CharField(max_length=100)
    category = models.ForeignKey('TransactionCategory', on_delete=models.CASCADE)

    board = models.ForeignKey('Board', on_delete=models.CASCADE)


    history = HistoricalRecords()


class TransactionCategory(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    history = HistoricalRecords()

    def statistic_by_date_range(self, start_date, end_date):
        pass
