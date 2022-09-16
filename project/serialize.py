from rest_framework import serializers
from .models import Package,DayDetails,Booking


class PackageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)  #image is not always required because we don't wanna
                                                  #update image every single time on updating some other data
    class Meta:
        model=Package
        fields="__all__"
class DayDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=DayDetails
        fields="__all__"

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields="__all__"


