from rest_framework import serializers
from cases_app.models import Cases
from donations_app.models import Donations
from donations_app.api.serializers import DonationSerializer

class CaseSerializer(serializers.ModelSerializer):
    donation_cases = serializers.SlugRelatedField(many=True, read_only=True, slug_field='donation_amount')
    total_donations = serializers.SerializerMethodField('get_total_donations')
    current_donations_amount = serializers.ReadOnlyField()
    def get_total_donations(self, obj):
        sum = 0
        query =  Donations.objects.filter(case_name=obj.id)
        for donation in query:
            sum += donation.donation_amount
        return sum
    class Meta:
        model = Cases
        fields = ['id', 'case_name', 'case_type', 'amount_needed', 'description', 
        'donation_cases', 'total_donations', 'current_donations_amount']
        # fields ='__all__'