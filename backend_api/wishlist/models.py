from djongo import models
from django.contrib.auth.models import User

from products.models import Website

class Wishlist(models.Model):

    mapping_id = models.IntegerField(default=0)
    brand = models.CharField(max_length=50)
    description = models.ListField(models.CharField(max_length=500))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    display_size = models.CharField(max_length=10)
    graphics_memory = models.CharField(max_length=30)
    img_link = models.URLField(max_length=10000)
    product_title = models.CharField(max_length=1000)
    ram = models.CharField(max_length=10)
    ram_type = models.CharField(max_length=100)
    storage = models.DictField()
    websites = models.ListField(
        models.EmbeddedModelField(
            model_container=Website
        )
    )



