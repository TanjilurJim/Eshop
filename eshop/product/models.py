from django.db import models

# Create your models here.
class Category(models.TextChoices): ##text choices used for dropdown

    ELECTRONICS = 'Electronics'
    LAPTOPS = 'Laptops'
    ARTS = 'arts'
    FOOD = 'food'
    HOME = 'Home'
    KITCHEN = 'Kitchen'


class Product(modesl.Model):
    name = models.CharField(max_length=200, default="", blank = False)
    description = models.TextField(max_length=1000, default="", blank=False)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    brand = models.CharField(max_length=200, default="", blank=False)
    category = models.CharField(max_length=30, choices=Category.choices) ## drop down categories will show

    


