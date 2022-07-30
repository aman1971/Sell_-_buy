from django.contrib import admin
from .models import Myproduct


admin.site.site_header = "Buy and Sell website"
admin.site.site_title = "Aman Buying"
admin.site.index_title = "Manage Aman Buying website"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','desc')
    search_fields = ('name',)

    def set_price_to_zero(self,request,queryset):
        queryset.update(price=0)

    actions = ("set_price_to_zero",)
    list_editable = ("price", "desc",)

# Register your models here.
admin.site.register(Myproduct, ProductAdmin)