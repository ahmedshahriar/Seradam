
from djongo import models


class Ryans(models.Model):
    brand = models.CharField(max_length=50)
    description = models.ListField(models.CharField(max_length=500))
    display_size = models.CharField(max_length=10)
    display_type = models.CharField(max_length=30)
    graphics_memory = models.CharField(max_length=30)
    img_link= models.URLField(max_length=10000)
    model = models.CharField(max_length=500)
    price = models.CharField(max_length=20)
    product_link = models.URLField(max_length=10000)
    product_title = models.CharField(max_length=1000)
    ram = models.CharField(max_length=10)
    ram_type = models.CharField(max_length=100)
    status = models.CharField(max_length=1000)
    storage = models.DictField()
    website = models.CharField(max_length=100)
    _id = models.CharField(primary_key=True, max_length=100)

    # def __str__(self):
    #     # return "<a href='" +  self.product_link + "' target='blank'>" + self.product_title + "</a><br/>"
    #     return self.product_title

class Startech(models.Model):
    brand = models.CharField(max_length=50)
    display_size = models.CharField(max_length=10)
    graphics_memory = models.CharField(max_length=30)
    img_link = models.URLField(max_length=10000)
    price = models.CharField(max_length=20)
    product_link = models.URLField(max_length=10000)
    product_title = models.CharField(max_length=1000)
    ram = models.CharField(max_length=10)
    ram_type = models.CharField(max_length=100)
    status = models.CharField(max_length=1000)
    storage = models.DictField()
    website = models.CharField(max_length=100)

    _id = models.CharField(primary_key=True, max_length=100)

    # def __str__(self):
    #     return str((self.brand))
    #     return "<a href='"+str( self.product_link)+"' target='blank'>"+self.product_title+"</a><br/>"



class Website(models.Model):
    website_name = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    product_link = models.URLField(max_length=10000)
    status = models.CharField(max_length=1000)


class Mapping(models.Model):
    brand = models.CharField(max_length=50)
    description = models.ListField(models.CharField(max_length=500))
    display_size = models.CharField(max_length=10)
    display_type = models.CharField(max_length=30)
    graphics_memory = models.CharField(max_length=30)
    img_link = models.URLField(max_length=10000)
    model = models.CharField(max_length=500)
    product_title = models.CharField(max_length=1000)
    ram = models.CharField(max_length=10)
    ram_type = models.CharField(max_length=100)
    storage = models.DictField()
    _id = models.CharField(primary_key=True, max_length=100)
    websites = models.ListField(
        models.EmbeddedModelField(
            model_container=Website
        )
    )

