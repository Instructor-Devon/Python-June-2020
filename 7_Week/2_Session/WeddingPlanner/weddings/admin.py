from django.contrib import admin
from .models import Wedding
# Register your models here.
class WeddingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Wedding, WeddingAdmin)