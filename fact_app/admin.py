from django.contrib import admin
from .models import Customer, Invoice, Article

class AdminCustomer(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'sex', 'city', 'zip_code')

class AdminInvoice(admin.ModelAdmin):
    list_display = ('customer', 'save_by', 'invoice_date', 'total', 'paid', 'invoice_type')

class AdminArticle(admin.ModelAdmin):
    list_display = ('invoice','name', 'quantity', 'unit_price', 'total')

admin.site.register(Customer, AdminCustomer)
admin.site.register(Invoice, AdminInvoice)
admin.site.register(Article, AdminArticle)