from rest_framework import serializers
from cases_app.models import Cases
from donations_app.api.serializers import DonationSerializer

class CaseSerializer(serializers.ModelSerializer):
    donation_cases = serializers.SlugRelatedField(many=True, read_only=True, slug_field='donation_amount')
    class Meta:
        model = Cases
        fields = ['id', 'case_name', 'case_type', 'amount_needed', 'description', 'donation_cases',]
        # fields ='__all__'