from django.contrib import admin
from .models import Ambassador


# Register your models here.

@admin.register(Ambassador)
class AmbassadorAdmin(admin.ModelAdmin):
    ...