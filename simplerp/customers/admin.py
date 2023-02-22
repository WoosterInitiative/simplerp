from django.contrib import admin

from simplerp.customers.models import Customer
from simplerp.globals.admin import BaseAdminModel


# Register your models here.
@admin.register(Customer)
class CustomerAdmin(BaseAdminModel):
    list_display = ["name", "phone"]
