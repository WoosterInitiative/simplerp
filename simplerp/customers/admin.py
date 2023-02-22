from django.contrib import admin

from customers.models import Customer
from globals.admin import BaseAdminModel


# Register your models here.
@admin.register(Customer)
class CustomerAdmin(BaseAdminModel):
    list_display = ["name", "phone"]
