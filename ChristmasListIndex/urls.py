from django.urls import path
from . import views

urlpatterns = [
    path('', views.buyer_view, name='gifter_view'),
    path('add/', views.list_item_form, name='list_item_form'),
    path('self/', views.owner_view, name='owner_view'),
    path('purchased/<int:id>', views.set_item_purchased, name='owner_view'),
    path('edit/<int:id>', views.edit_item, name='edit'),
    path('delete/<int:id>', views.delete_item, name='delete'),
    path('test', views.test, name='test'),
    
]