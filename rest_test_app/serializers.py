from rest_framework import serializers

from .models import Car

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ('brand', 'color')