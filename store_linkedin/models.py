from django.db import models

# Create your models here.
class Company(models.Model):

    company_name=models.CharField(max_length=60)

    company_descrition =models.TextField(null=True)

class Employeed(models.Model):
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)

    employeed_first_name=models.CharField(max_length=43)

    employeed_last_name=models.CharField(max_length=43)

    company_position=models.CharField(max_length=43)