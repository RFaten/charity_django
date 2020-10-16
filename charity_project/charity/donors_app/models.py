from django.db import models

# Create your models here.
class Donors(models.Model):
    donor_name = models.CharField(max_length=264, unique=True)
    phone_number = models.CharField(max_length=264)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.donor_name
