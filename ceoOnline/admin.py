from django.contrib import admin
from .models import *
# Register your models here.

class admintb(admin.ModelAdmin):
    raw_input=('didian',)


admin.site.register(user)
admin.site.register(news)
admin.site.register(friend)
admin.site.register(setting)
admin.site.register(tb_prov_city_area_street,admintb)
