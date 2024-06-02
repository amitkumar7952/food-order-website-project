from django.contrib import admin
from .models import Contact
from .models import Order
class contactadmin(admin.ModelAdmin):
    list_display=('name','email','phone')
    search_fields=('name',)
# Register your models here.
admin.site.register(Contact,contactadmin)
class orderadmin(admin.ModelAdmin):
    list_display=('name','email','phone','address','food','quantity')
    search_fields=('name','food')
    admin.site.register(Order,)