from rest_framework import serializers
from .models import WeightClass, Fighter, Event, Bout

class WeightClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightClass
        fields = '__all__'

class FighterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fighter
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class BoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bout
        fields = '__all__'
