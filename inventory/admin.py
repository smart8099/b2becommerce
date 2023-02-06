from django.contrib import admin
from inventory.models import Product, CompanyProfile

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    # list_display = ['customer', 'total_cost', 'order_date', 'status']

    def save_model(self, request, obj, form, change):
        obj.total_cost = obj.calculate_total_cost()
        super().save_model(request, obj, form, change)


#admin.site.register(Order, OrderAdmin)

admin.site.register(Product)
# admin.site.register(Order)
admin.site.register(CompanyProfile)
