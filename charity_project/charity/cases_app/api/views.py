from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from cases_app.models import Cases
from cases_app.api.serializers import CaseSerializer
from django.http import JsonResponse

@api_view(['GET',])
def api_list_cases(request):
    case_list = Cases.objects.all()
    serializer = CaseSerializer(case_list, many=True)
    # return JsonResponse(serializer.data, safe=False)
    return Response(serializer.data)

@api_view(['PUT',])
def api_update_case(request, id):
    try:
        # caseObj = get_object_or_404(Cases, id = id)
        caseObj = Cases.objects.get(id=id)
    except Cases.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CaseSerializer(caseObj, data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        data['success'] = "Update successful"
        return Response(data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE',])
def api_delete_case(request, id):
    try:
        caseObj = Cases.objects.get(id=id)
    except Cases.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    operation = caseObj.delete()
    data = {}
    if operation:
        data['success'] = "delete successful"
    else:
        data['failure'] = "delete failed"
   
    return Response(data=data)

@api_view(['POST', ])
def api_create_case(request):
    caseObj = Cases()
    serializer = CaseSerializer(caseObj, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)