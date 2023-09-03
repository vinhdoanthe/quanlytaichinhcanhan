from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from apps.transaction.models import Board


class BoardListView(LoginRequiredMixin, ListView):
    model = Board
    template_name = 'board_list.html'
    context_object_name = 'boards'

    def get_queryset(self):
        return Board.objects.filter(user=self.request.user)


class BoardCreateView(LoginRequiredMixin, CreateView):
    model = Board
    template_name = 'board_create.html'
    fields = ['name', 'description', 'start_date', 'end_date']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BoardDetailView(LoginRequiredMixin, DetailView):
    model = Board
    template_name = 'board_detail.html'
    context_object_name = 'board'


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
