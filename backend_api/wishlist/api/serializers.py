from rest_framework import serializers
from wishlist.models import *



# class WishlistSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Wishlist
#
#         fields = ("website_name", "product_link", "price", 'user')


class WishlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wishlist

        fields = ("mapping_id", "brand", "user", "display_size", "graphics_memory", "product_title",
                  "img_link", "ram", "ram_type", "storage", "websites", "description", "id")

