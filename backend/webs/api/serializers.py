from rest_framework import serializers
from webs.models import *


# class RyansSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ryans
#         fields = ('_id','product_title', 'price')


class StartechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startech
        fields = ('product_title', 'price','brand','product_link')

class RyansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ryans
        fields = ('product_title', 'price','brand','product_link')
