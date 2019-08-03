from rest_framework import serializers
from wishlist.models import *



class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist

        fields = ("website_name", "product_link", "price", 'user')



