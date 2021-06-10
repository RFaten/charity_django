from rest_framework import serializers
from donations_app.models import Donations

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donations
        fields = '__all__'