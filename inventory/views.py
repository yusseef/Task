from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, UpdateView, DeleteView
from .forms import InventoryForm
from .models import Inventory
# Create your views here.


def inventory_list_view(request):
    products = Inventory.objects.all()
    context = {'object_list': products}
    return render(request, 'list_inventory.html', context = context)

def inventory_search_view(request):
    query = request.GET.get('q')
    product_search = Inventory.objects.filter(name__icontains = query)
    context = {'object_list': product_search}
    return render(request, 'inventory_search.html', context = context)

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