from django.db import models
# from phone_field import PhoneField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Donors(models.Model):
    donor_name = models.CharField(max_length=264, unique=True)
    # phone_number = PhoneField(blank=True, help_text='Contact phone number')
    phone_number = PhoneNumberField()
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.donor_name
