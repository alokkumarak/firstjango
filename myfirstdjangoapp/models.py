from django.db import models

# Create your models here.
class mydetails(models.Model):
    name=models.CharField(max_length=200)
    number=models.IntegerField()
    college_name=models.CharField(max_length=50)
    description=models.TextField()
