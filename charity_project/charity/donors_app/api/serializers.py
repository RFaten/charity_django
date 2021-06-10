from rest_framework import serializers
from donors_app.models import Donors

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donors
        fields ='__all__'