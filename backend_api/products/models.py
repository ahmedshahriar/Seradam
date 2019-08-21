from djongo import models
from django.contrib.auth.models import User
from datetime import datetime

class Ryans(models.Model):
    brand = models.CharField(max_length=50)
    description = models.ListField(models.CharField(max_length=1000))
    display_size = models.CharField(max_length=10)
    display_type = models.CharField(max_length=30)
    graphics_memory = models.CharField(max_length=30)
    img_link = models.URLField(max_length=10000)
    model = models.CharField(max_length=500)
    price = models.IntegerField(default=0)
    product_link = models.URLField(max_length=10000)
    product_title = models.CharField(max_length=1000)
    ram = models.CharField(max_length=10)
    ram_type = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    storage = models.DictField()
    website = models.CharField(max_length=100)
    _id = models.CharField(primary_key=True, max_length=100)

    # def __str__(self):
    #     # return "<a href='" +  self.product_link + "' target='blank'>" + self.product_title + "</a><br/>"
    #     return self.product_title




class Startech(models.Model):
    brand = models.CharField(max_length=50)
    description = models.ListField(models.CharField(max_length=1000))
    display_size = models.CharField(max_length=10)
    graphics_memory = models.CharField(max_length=30)
    img_link = models.URLField(max_length=10000)
    price = models.IntegerField(default=0)
    product_link = models.URLField(max_length=10000)
    product_title = models.CharField(max_length=1000)
    ram = models.CharField(max_length=10)
    ram_type = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    storage = models.DictField()
    website = models.CharField(max_length=100)
    _id = models.CharField(primary_key=True, max_length=100)
    # def __str__(self):
    #     # return "<a href='" +  self.product_link + "' target='blank'>" + self.product_title + "</a><br/>"
    #     return self.product_title



class Website(models.Model):
    website_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    product_link = models.URLField(max_length=10000)
    status = models.CharField(max_length=1000)
    img_link = models.URLField(max_length=10000)


class Mapping(models.Model):

    brand = models.CharField(max_length=50)
    description = models.ListField(models.CharField(max_length=500))
    display_size = models.CharField(max_length=10)
    graphics_memory = models.CharField(max_length=30)
    img_link = models.URLField(max_length=10000)
    product_title = models.CharField(max_length=1000)
    ram = models.CharField(max_length=10)
    ram_type = models.CharField(max_length=100)
    storage = models.DictField()
    _id = models.CharField(max_length=100)
    websites = models.ListField(
        models.EmbeddedModelField(
            model_container=Website
        )
    )
    id = models.IntegerField(primary_key=True)


class Search(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    search_count = models.IntegerField(default=0)


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_title = models.CharField(max_length=1000)
    product_link = models.URLField(max_length=1000)
    website_name = models.CharField(max_length=100)
    old_price = models.IntegerField(default=0)
    new_price = models.IntegerField(default=0)
    seen = models.BooleanField(default=False)


class SearchHit(models.Model):
    date = models.DateTimeField(default=datetime.now)
    count = models.IntegerField(default=0)


class UserActivity(models.Model):
    date = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
