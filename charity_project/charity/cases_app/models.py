from django.db import models

# Create your models here.
class Cases(models.Model):
    case_name = models.CharField(max_length=264, unique=True)
    case_type = models.CharField(max_length=264)
    amount_needed = models.PositiveIntegerField()
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.case_name
