from django.urls import path
from .views import *
urlpatterns = [
    path('', inventory_list_view, name = 'inventory-list'),
    path('search/', inventory_search_view, name = 'inventory-search'),
    path('test', IndexView.as_view(), name = 'test'),
    path('create/', Inventory_createView.as_view(), name = 'inventory-create'),
    path('update/<str:pk>', Inventory_updateView.as_view(), name = 'inventory-update'),
    path('delete/<str:pk>', Inventory_deleteView.as_view(), name = 'inventory-delete'),



]