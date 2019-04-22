from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'url_key', 'status', 'categories', 'price', 'special_price',)
    list_display = ('title','url_key', 'status', 'formatted_price',)

    def formatted_price(self, obj):
        return "${}".format(obj.price)

class CategoryAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'url_key', 'status',)
    list_display = ('title','url_key', 'status',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
