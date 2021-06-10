from django.db import models
from cases_app.models import Cases
from donors_app.models import Donors

# Create your models here.
class Donations(models.Model):
    donor_name = models.ForeignKey(Donors, on_delete=models.SET_NULL, null=True)
    case_name = models.ForeignKey(Cases, on_delete=models.SET_NULL, null=True, related_name='donation_cases')
    donation_amount = models.PositiveIntegerField()
    paid_flag = models.BooleanField()

    def __str__(self):
        return self.case_name.case_name + ' / ' + str(self.donation_amount)

