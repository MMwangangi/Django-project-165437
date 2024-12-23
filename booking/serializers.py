from rest_framework import serializers
from .models import Flight, Passenger
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

class PassengerSerializer(serializers.ModelSerializer):
    flight = FlightSerializer(read_only=True)

    class Meta:
        model = Passenger
        fields = '__all__' 