from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


# Create your models here.
class BaseModel(models.Model):
    name = models.CharField(_("name"), max_length=50)
    slug = models.SlugField(_("slug"))
    created_date = models.DateTimeField(_("created date"), auto_now_add=True)
    created_by = models.ForeignKey(
        "settings.AUTH_USER_MODEL",
        verbose_name=_("created by"),
        on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_created",
        editable=False,
    )
    modified_date = models.DateTimeField(_("modified date"), auto_now=True)
    modified_by = models.ForeignKey(
        "settings.AUTH_USER_MODEL",
        verbose_name=_("modified by"),
        on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_created",
        editable=False,
    )

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)
