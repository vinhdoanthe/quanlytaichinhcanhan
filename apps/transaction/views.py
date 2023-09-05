from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    DeleteView,
    FormView,
    UpdateView,
)
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormMixin

from apps.transaction.forms import BoardForm, TransactionForm
from apps.transaction.models import (
    Board,
    Transaction,
)
from apps.transaction.tables import (
    BoardTable,
    TransactionTable,
)
from django_tables2 import SingleTableView


class BoardListView(LoginRequiredMixin, SingleTableView):
    model = Board
    template_name = 'transaction/board_list.html'
    table_class = BoardTable

    paginate_by = 10

    def get_queryset(self):
        return Board.objects.filter(user=self.request.user).order_by('-id')


class BoardCreateView(LoginRequiredMixin, FormView):
    model = Board
    template_name = 'transaction/board.html'
    form_class = BoardForm
    success_url = reverse_lazy('board_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class BoardDetailView(LoginRequiredMixin, SingleObjectMixin, SingleTableView, FormMixin):
    model = Board
    template_name = 'transaction/board_detail.html'
    table_class = TransactionTable
    context_object_name = 'board'
    form_class = TransactionForm

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return Board.objects.get(pk=self.kwargs['pk'])

    def get_queryset(self):
        return Transaction.objects.filter(board=self.kwargs['pk'])

    def get_success_url(self):
        return reverse_lazy('board_detail', kwargs={'pk': self.kwargs['pk']})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        form.instance.board = self.object
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class BoardUpdateView(LoginRequiredMixin, UpdateView):
    model = Board
    template_name = 'board_update.html'
    fields = ['name', 'description', 'start_date', 'end_date']
    context_object_name = 'board'


class BoardDeleteView(LoginRequiredMixin, DeleteView):
    model = Board
    template_name = 'board_delete.html'
    success_url = reverse_lazy('board_list')
    context_object_name = 'board'
