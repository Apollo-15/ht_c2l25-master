from django.contrib import admin

from .models import IceCream, Image

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class IceCreamAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(Image)
