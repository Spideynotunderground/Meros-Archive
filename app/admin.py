from django.contrib import admin
from .models import Ambassador, Story, StoryImage


# Register your models here.

@admin.register(Ambassador)
class AmbassadorAdmin(admin.ModelAdmin):
    ...

class StoryImageInline(admin.TabularInline):
    model = StoryImage  # 👈 This must be a model class, not an instance or something else
    extra = 6

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    inlines = [StoryImageInline]