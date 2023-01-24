from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, UpdateView, DeleteView
from .forms import InventoryForm
from .models import Inventory
# Create your views here.

class InventoryListView(ListView):
    model = Inventory
    template_name = 'list_inventory.html'


class IndexView(ListView):
    model = Inventory
    template_name = 'test.html'

class Inventory_createView(FormView):
    form_class = InventoryForm
    template_name = 'create_inventory.html'
    success_url = '/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class Inventory_updateView(UpdateView):
    model = Inventory
    fields = '__all__'
    success_url = '/'
    template_name = 'update_inventory.html'

class Inventory_deleteView(DeleteView):
    model = Inventory
    success_url = '/'
    template_name = 'delete_inventory.html'