from django.contrib import admin


# Register your models here.
class BaseAdminModel(admin.ModelAdmin):
    class Meta:
        abstract = True

    def save_model(self, request, obj, form, change) -> None:
        if not change:
            obj.created_by = request.user

        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)
