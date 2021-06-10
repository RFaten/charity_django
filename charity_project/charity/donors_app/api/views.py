from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from donors_app.models import Donors
from donors_app.api.serializers import DonorSerializer
from django.http import JsonResponse

@api_view(['GET',])
def api_list_donors(request):
    donor_list = Donors.objects.all()
    serializer = DonorSerializer(donor_list, many=True)
    return Response(serializer.data)

@api_view(['PUT',])
def api_update_donor(request, id):
    try:
        donorObj = Donors.objects.get(id=id)
    except Donors.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = DonorSerializer(donorObj, data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        data['success'] = "Update successful"
        return Response(data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE',])
def api_delete_donor(request, id):
    try:
        donorObj = Donors.objects.get(id=id)
    except Donors.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    operation = donorObj.delete()
    data = {}
    if operation:
        data['success'] = "delete successful"
    else:
        data['failure'] = "delete failed"
   
    return Response(data=data)

@api_view(['POST', ])
def api_create_donor(request):
    donorObj = Donors()
    serializer = DonorSerializer(donorObj, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)