from pops.models import Pop, PopDevice, PopDeviceState
from django.contrib import admin


class PopAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'code', 'name', 'latitude', 'longitude', 'network_status', 'user', 'is_active']
    list_per_page = 20


admin.site.register(Pop, PopAdmin)


class PopDeviceAdmin(admin.ModelAdmin):
    list_display = ['id', 'pop_name', 'status', 'code', 'name', 'is_active']
    list_per_page = 20


admin.site.register(PopDevice, PopDeviceAdmin)


class PopDeviceStateAdmin(admin.ModelAdmin):
    list_display = ['id', 'device_code', 'topic', 'date', 'is_active']
    list_per_page = 20


admin.site.register(PopDeviceState, PopDeviceStateAdmin)



    