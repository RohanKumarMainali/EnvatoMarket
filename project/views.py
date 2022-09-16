from .models import Package
from  . import serialize
from .serialize import PackageSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required

from rest_framework import permissions



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))

def package_list(request):
    SinglePackage=Package.objects.all()
    serializeObj=PackageSerializer(SinglePackage,many='true')
    return Response(serializeObj.data)


@api_view(['POST'])
def create_package(request):
    serializeObj=PackageSerializer(data=request.data)
    if serializeObj.is_valid():
        serializeObj.save()
    return Response(serializeObj.data)

@api_view(['PATCH'])
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
def delete_package(request,pk):
    SinglePackage=Package.objects.get(id=pk)
    SinglePackage.delete()

    return Response("Package Deleted Successfully")

