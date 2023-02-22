from address.models import AddressField
from django.db import models
from django.utils.translation import gettext_lazy as _
from globals.models import BaseModel
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Customer(BaseModel):
    business = models.CharField(
        _("business"), help_text=_("optional"), max_length=50, blank=True
    )
    shipping_address = AddressField(
        verbose_name=_("shipping address"), related_name="shipping"
    )
    billing_address = AddressField(
        verbose_name=_("billing address"), related_name="billing"
    )
    phone = PhoneNumberField(_("phone"))
