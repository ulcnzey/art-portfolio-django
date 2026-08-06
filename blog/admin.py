from django.contrib import admin
from .models import Portfolio, ExtraGallery, Service


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')  
    list_filter = ('category',)
    search_fields = ('title', 'category')


class ExtraGalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  
    search_fields = ('title', 'description')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_class', 'created_at')
    search_fields = ('title', 'description')    


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(ExtraGallery, ExtraGalleryAdmin)
admin.site.register(Service, ServiceAdmin)
