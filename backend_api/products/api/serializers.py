from rest_framework import serializers
from products.models import *



class StartechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startech

        fields = ('brand', "description", 'display_size','graphics_memory', 'img_link', 'price', 'product_link', 'product_title',
                  'ram','ram_type', "processor",'status','storage', 'website')


class RyansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ryans
        fields = ( 'brand', 'display_size', 'graphics_memory', 'img_link', 'price', 'product_link', 'product_title',
                  'ram', 'ram_type',"processor", 'status', 'storage',  'description','model', 'website')


class MappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mapping

        fields = ("brand", "description", "display_size", "graphics_memory", "img_link",
                  "product_title", "ram", "ram_type", "storage", "websites","id")


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification

        fields = ("user","product_title","product_link",
                  "website_name","old_price","new_price","seen")

# class BrandSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Mapping
#         fields = ("brand",)
#
#


class BrandSerializer(serializers.Serializer):

    brand = serializers.CharField(max_length=50)





class AdminSerializer(serializers.Serializer):

    total_brands = serializers.IntegerField(default=0)
    total_products = serializers.IntegerField(default=0)
    total_websites = serializers.IntegerField(default=0)
    total_users = serializers.IntegerField(default=0)


class SearchWishlistSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    search_count = serializers.IntegerField(default=0)
    wishlist_count = serializers.IntegerField(default=0)


class NotificationWishlistCountSerializer(serializers.Serializer):

    notification_count = serializers.IntegerField(default=0)
    wishlist_count = serializers.IntegerField(default=0)


class SearchHitSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchHit
        fields = ("date","count")