from django.urls import path

from apps.transaction import views

urlpatterns = [
    path('boards/', views.BoardListView.as_view(), name='board_list'),
    path('boards/create/', views.BoardCreateView.as_view(), name='board_create'),
    path('boards/<int:pk>/', views.BoardDetailView.as_view(), name='board_detail'),
    path('boards/<int:pk>/update/', views.BoardUpdateView.as_view(), name='board_update'),
    path('boards/<int:pk>/delete/', views.BoardDeleteView.as_view(), name='board_delete'),
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
]
