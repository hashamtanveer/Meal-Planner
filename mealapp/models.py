from django.db import models

# Create your models here.
class Ingredients(models.Model):
    recipe_name = models.CharField(max_length=255)
    ingredient_1 = models.CharField(max_length=255)
    ingredient_2 = models.CharField(max_length=255)
    ingredient_3 = models.CharField(max_length=255)
    ingredient_4 = models.CharField(max_length=255)
    ingredient_5 = models.CharField(max_length=255)


class Diet_Types(models.Model):
    recipe_name = models.CharField(max_length=255)
    diet_type_1 = models.CharField(max_length=255)
    diet_type_2 = models.CharField(max_length=255)
    diet_type_3 = models.CharField(max_length=255)
    diet_type_4 = models.CharField(max_length=255)
    diet_type_5 = models.CharField(max_length=255)
