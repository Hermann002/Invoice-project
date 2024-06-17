from django.shortcuts import render
from django.views import View
from .models import Invoice

# Create your views here.

class HomeView(View):
    """ Main View """

    templates_name = 'index.html'

    invoices = Invoice.objects.select_related('customer', 'save_by').all()

    context = {
        'invoices': invoices
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.templates_name, self.context)
    
    def post(self, request, *args, **kwargs):
        return render(request, self.templates_name, self.context)
    
class AddCustomerView(View):
    """ Add new customer """
    template_name = "add_customer.html"

    def get(self, request, *args, **kwagrs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwagrs):
        print(request.POST)
        return render(request, self.template_name)