from django.contrib import admin
from .models import Category, Product, FooterInfo
from django.utils.safestring import mark_safe

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'photo_img_tag', 'category', 'is_visible', 'sort', 'description')
    list_display_links = ('id', 'name')
    list_editable = ('price', 'category', 'is_visible', 'sort')
    list_filter = ('category','is_visible', 'sort')
    search_fields = ('name',)

    def photo_img_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width='50'>")


class ProductInLine(admin.TabularInline):
    model = Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        ProductInLine,
    ]


admin.site.register(FooterInfo)