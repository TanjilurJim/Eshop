from django.db import models
from django.contrib.auth.models import User

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
    ratings = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    stock = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) #To create a relationship with the user. Set_null is used beacuse if the user is deleted don't delete the product just make the user null
    createdAt = models.DateTimeField(auto_now_add=True) # new product will automatically create date and time

    



