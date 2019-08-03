from djongo import models
from django.contrib.auth.models import User


class Wishlist(models.Model):

    website_name = models.CharField(max_length=100)
    product_link = models.URLField(max_length=1000)
    price = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
