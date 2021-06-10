from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from donations_app.models import Donations
from donations_app.api.serializers import DonationSerializer
from django.http import JsonResponse
from django.db.models import Count, Sum

@api_view(['GET',])
def api_list_donations(request):
    # donation_list = Donations.objects.all().annotate(donation_amount_sum = Sum('donation_amount'))
    # donation_list = Donations.objects.values('case_name').annotate(dcount=Count('case_name'))
    donation_list = Donations.objects.all()
    serializer = DonationSerializer(donation_list, many=True)
    return Response(serializer.data)

# @api_view(['PUT',])
# def api_update_donation(request, id):
#     try:
#         donorObj = Donors.objects.get(id=id)
#     except Donors.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     serializer = DonorSerializer(donorObj, data=request.data)
#     data = {}
#     if serializer.is_valid():
#         serializer.save()
#         data['success'] = "Update successful"
#         return Response(data=data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE',])
# def api_delete_donation(request, id):
#     try:
#         donorObj = Donors.objects.get(id=id)
#     except Donors.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     operation = donorObj.delete()
#     data = {}
#     if operation:
#         data['success'] = "delete successful"
#     else:
#         data['failure'] = "delete failed"
   
#     return Response(data=data)

@api_view(['POST', ])
def api_create_donation(request):
    donorObj = Donors()
    serializer = DonorSerializer(donorObj, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)