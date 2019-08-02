from rest_framework import serializers
from webs.models import *

#
class StartechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startech

        fields = ('brand', 'display_size','graphics_memory', 'img_link', 'price', 'product_link', 'product_title',
                  'ram','ram_type','status','storage', 'website')


class RyansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ryans
        fields = ('_id', 'brand', 'display_size', 'graphics_memory', 'img_link', 'price', 'product_link', 'product_title',
                  'ram', 'ram_type', 'status', 'storage',  'description','model', 'website')


class MappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mapping

        fields = ("brand", "description", "display_size", "display_type", "graphics_memory", "img_link", "model",
                   "product_title", "ram", "ram_type", "storage", "websites")

