from django.db import models

# Create your models here.
class Cases(models.Model):
    case_name = models.CharField(max_length=264, unique=True)
    case_type = models.CharField(max_length=264)
    amount_needed = models.PositiveIntegerField()
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.case_name

    @property
    def current_donations_amount(self):
        sum = 0
        donation_list = self.donation_cases.all()
        for donation in donation_list:
            sum += donation.donation_amount
        return sum
