from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Flight, Booking


class FlightSerializer(serializers.ModelSerializer):
	class Meta:
		model = Flight
		fields = ['destination', 'time', 'price', 'id']


class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['flight', 'date', 'id']


class BookingDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['flight', 'date', 'passengers', 'id']


class UpdateBookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['date', 'passengers']

class UserCreateSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	class Meta:
		model = User
		fields = ['username', 'password', 'last_name','first_name',]

	# def create(self, validated_data):
	#     myusername = validated_data['username']
	#     mypassword = validated_data['password']
	#     mylast_name= validated_data['last_name']
	#     myfirst_name= validated_data['first_name']
	#     new_user = User(username=myusername, last_name=mylast_name,first_name=myfirst_name)
	#     new_user.set_password(mypassword)
	#     new_user.save()
	#     return validated_data

		def create(self, validated_data):

			new_user = User(**validated_data)
			new_user.set_password(validated_data['password'])
			new_user.save()

			return validated_data