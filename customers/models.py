from django.db import models


class CustomerDetails(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    email = models.EmailField(max_length=200, null=False)
    platform = models.CharField(max_length=50, null=True)
    phoneNumber = models.CharField(max_length=50, null=False)
    address=models.CharField(max_length=150, null=False)
    user = models.CharField(max_length=200, null=False)
