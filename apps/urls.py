from django.urls import path

from apps.transaction import views as transaction_views

urlpatterns = [
    path('', transaction_views.BoardListView.as_view(), name='board_list'),
]
