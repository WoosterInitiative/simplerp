from address.models import AddressField
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from simplerp.globals.models import BaseModel


# Create your models here.
class Customer(BaseModel):
    business = models.CharField(
        _("business"), help_text=_("optional"), max_length=50, blank=True
    )
    shipping_address = AddressField(verbose_name=_("shipping address"))
    billing_address = AddressField(verbose_name=_("billing address"))
    phone = PhoneNumberField(_("phone"))
