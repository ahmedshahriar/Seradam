
from djongo import models


class Ryans(models.Model):

    product_title = models.CharField(max_length=1000)
    product_link = models.URLField(max_length=1000)
    img_link = models.URLField(max_length=1000)
    price = models.CharField(max_length=20)
    model = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    brand = models.CharField(max_length=100)

    _id = models.CharField(primary_key=True, max_length=100)

    def __str__(self):
        return "<a href='" + self.product_link + "' target='blank'>" + self.product_title + "</a><br/>"


class Startech(models.Model):

    product_title = models.CharField(max_length=1000)
    product_link = models.URLField(max_length=1000)
    img_link = models.URLField(max_length=1000)
    price = models.CharField(max_length=30)
    status = models.CharField(max_length=20)
    brand = models.CharField(max_length=100)

    _id = models.CharField(primary_key=True, max_length=100)
    def __str__(self):
        return "<a href='"+self.product_link+"' target='blank'>"+self.product_title+"</a><br/>"

class Mapping(models.Model):
    _id = models.CharField(primary_key=True, max_length=100)
    ryans = models.ForeignKey(Ryans,on_delete=models.CASCADE, db_column='ryans')
    startech = models.ForeignKey(Startech,on_delete=models.CASCADE, db_column='startech')