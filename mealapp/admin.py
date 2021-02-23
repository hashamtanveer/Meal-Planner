from django.contrib import admin
from mealapp.models import Ingredients

# Register your models here.

@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    pass

from mealapp.models import Diet_Types
@admin.register(Diet_Types)
class IngredientsAdmin(admin.ModelAdmin):
    pass
