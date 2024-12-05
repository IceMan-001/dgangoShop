from django.contrib import admin
from .models import Category, Product, Gallery

class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = Gallery


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Попытка загрузки нескольких картинок товара"""

    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}  # вычисляемые поля


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'description', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [GalleryInline, ]




# class GalleryInline(admin.TabularInline):
#     fk_name = 'product'
#     model = Gallery
#
#
# @admin.register(Product)
# class ProductAdminImage(admin.ModelAdmin):
#     inlines = [GalleryInline, ]
