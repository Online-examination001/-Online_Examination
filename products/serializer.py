from rest_framework import serializers
from .models import Products

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = [
            'pk',
            'title',
            'unique_id',
            'description',
            'price',
            'user',
            'date_added',
            'date_updated',
            'slug'
        ]
        read_only_field = ['pk','date_added','slug']