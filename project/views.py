from .models import Package,Booking,DayDetails
from  . import serialize
from .serialize import PackageSerializer,BookingSerializer, DayDetailsSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required

from rest_framework import permissions


#  API for package

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))

def package_list(request):
    SinglePackage=Package.objects.all()
    serializeObj=PackageSerializer(SinglePackage,many='true')
    return Response(serializeObj.data)

# get single package
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))

def package(request,pk):
    package=Package.objects.filter(id=pk)
    serializeObj=PackageSerializer(package,many='true')
    return Response(serializeObj.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))

def create_package(request):
    serializeObj=PackageSerializer(data=request.data)
    if serializeObj.is_valid():
        serializeObj.save()
    return Response(serializeObj.data)

@api_view(['PATCH'])
@permission_classes((permissions.AllowAny,))

def update_package(request,pk):

    SinglePackage=Package.objects.get(id=pk)

    serializeObj=PackageSerializer(instance=SinglePackage,data=request.data)
    data={}
    if serializeObj.is_valid():
        serializeObj.save()
        data["success"]="update succesfully"
        return Response(data=data)

    return Response(serializeObj.errors)
#
@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))

def delete_package(request,pk):
    SinglePackage=Package.objects.get(id=pk)
    SinglePackage.delete()

    return Response("Package Deleted Successfully")

#API for DayDetails

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))

def day_details(request):
    day=DayDetails.objects.all()
    serializeObj=DayDetailsSerializer(day,many='true')
    return Response(serializeObj.data)

# Single package day details
# @api_view(['GET'])
# @permission_classes((permissions.AllowAny,))
# def package_day_details(request,package_name):
#     day_details=Package.objects.filter(name=package_name)
#     serializeObj=DayDetailsSerializer(package,many='true')
#     return Response(serializeObj.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))

def create_day_details(request):
    serializeObj=DayDetailsSerializer(data=request.data)
    if serializeObj.is_valid():
        serializeObj.save()
    return Response(serializeObj.data)

@api_view(['PATCH'])
@permission_classes((permissions.AllowAny,))

def update_day_details(request,pk):

    day=DayDetails.objects.get(id=pk)

    serializeObj=PackageSerializer(instance=day,data=request.data)
    data={}
    if serializeObj.is_valid():
        serializeObj.save()
        data["success"]="update succesfull!"
        return Response(data=data)

    return Response(serializeObj.errors)
#
@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))

def delete_day_details(request,pk):
    day=DayDetails.objects.get(id=pk)
    day.delete()

    return Response("Day Details Deleted Successfully")


#API for booking

#API for DayDetails

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))

def booking(request):
    booking=Booking.objects.all()
    serializeObj=BookingSerializer(booking,many='true')
    return Response(serializeObj.data)

# Single booking details
# @api_view(['GET'])
# @permission_classes((permissions.AllowAny,))
# def single_booking(request,pk):
#     booking=Booking.objects.filter(id=pk)
#     serializeObj=BookingSerializer(package,many='true')
#     return Response(serializeObj.data)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))

def create_booking(request):
    serializeObj=DayDetailsSerializer(data=request.data)
    if serializeObj.is_valid():
        serializeObj.save()
    return Response(serializeObj.data)

@api_view(['PATCH'])
@permission_classes((permissions.AllowAny,))

def update_booking(request,pk):

    booking=Booking.objects.get(id=pk)
    serializeObj=BookingSerializer(instance=booking,data=request.data)
    data={}
    if serializeObj.is_valid():
        serializeObj.save()
        data["success"]="update succesfull!"
        return Response(data=data)

    return Response(serializeObj.errors)

@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))

def delete_booking(request,pk):
    booking=Booking.objects.get(id=pk)
    booking.delete()

    return Response("Day Details Deleted Successfully")




