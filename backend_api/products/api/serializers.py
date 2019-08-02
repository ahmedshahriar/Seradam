from rest_framework import serializers
from products.models import *

#
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
                  "product_title", "ram", "ram_type", "storage", "websites")

