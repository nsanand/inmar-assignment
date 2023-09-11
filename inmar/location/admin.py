from django.contrib import admin

from .models import (
    Location,
    Department,
    Category,
    SubCategory,
    MetaData,
    SKUData,
)


class MetaDataAdmin(admin.ModelAdmin):
    """
    Admin class for UploadMarksData Model
    """
    list_display = (
        "location", "department", "category", "sub_category"
    )

    search_fields = (
        "location__name", "department__name",  "category__name", "sub_category__name"
    )


class SKUDataAdmin(admin.ModelAdmin):
    """
    Admin class for UploadMarksData Model
    """
    list_display = (
        "sku", "name", "location", "department", "category", "sub_category"
    )

    search_fields = (
        "sku", "name", "location__name", "department__name",  "category__name", "sub_category__name"
    )


admin.site.register(Location)
admin.site.register(Department)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(MetaData, MetaDataAdmin)
admin.site.register(SKUData, SKUDataAdmin)
