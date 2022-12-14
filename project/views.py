from .models import *
from  . import serialize
from .serialize import *
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
    package=Package.objects.filter(name=pk)
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



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def package_day_details(request,_id):
    day_details=DayDetails.objects.filter(package=_id)
    serializeObj=DayDetailsSerializer(day_details,many='true')
    return Response(serializeObj.data)

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


    # ----------------------------------------------------------------

# API for FAQs

# Single FAQ



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def package_FAQ(request,_id):
    FAQs=FAQ.objects.filter(package=_id)
    serializeObj=FAQSerializer(FAQs,many='true')
    return Response(serializeObj.data)


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

# API for testimonial

#GET testimonial


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))

def testimonial(request):
    testimonial=Testimonial.objects.all()
    serializeObj=TestimonialSerializer(testimonial,many='true')
    return Response(serializeObj.data)

#POST testimonial

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))

def create_testimonial(request):
    serializeObj=TestimonialSerializer(data=request.data)
    if serializeObj.is_valid():
        serializeObj.save()
    return Response(serializeObj.data)

#UPDATE Testimonial


@api_view(['PATCH'])
@permission_classes((permissions.AllowAny,))

def update_testimonial(request,pk):
    testimonial=Testimonial.objects.get(id=pk)
    serializeObj=TestimonialSerializer(instance=booking,data=request.data)
    data={}
    if serializeObj.is_valid():
        serializeObj.save()
        data["success"]="update succesfull!"
        return Response(data=data)

    return Response(serializeObj.errors)

# Delete testimonial

@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))

def delete_testimonial(request,pk):
    testimonial=Testimonial.objects.get(id=pk)
    testimonial.delete()

    return Response("Day Details Deleted Successfully")

#API for blog post

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))

def blog(request):
    blog=Blog.objects.all()
    serializeObj=BlogSerializer(blog,many='true')
    return Response(serializeObj.data)
