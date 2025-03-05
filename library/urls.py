from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('add/', views.book_add, name='book_add'),
    path('checkout/<int:book_id>/', views.book_checkout, name='book_checkout'),
    path('return/<int:transaction_id>/', views.book_return, name='book_return'),
    path('register/', views.member_register, name='member_register'),
]
