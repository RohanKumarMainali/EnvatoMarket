from rest_framework import serializers
from .models import *


class PackageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)  #image is not always required because we don't wanna
    category = serializers.StringRelatedField()
    class Meta:
        model=Package
        fields="__all__"
    def get_category_name(self, category):
        return category.name

class DayDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=DayDetails
        fields="__all__"

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields="__all__"

class TestimonialSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)  
    class Meta:
        model=Testimonial
        fields="__all__"

class BlogSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)  
    class Meta:
        model=Blog
        fields="__all__"


