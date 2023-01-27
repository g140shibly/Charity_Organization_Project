from django.db import models

class Charity(models.Model):
    org_name=models.CharField(max_length=50)
    method=models.CharField(max_length=100)
    email=models.EmailField(max_length=30)
    nav_factor=models.IntegerField()

    class Meta:
        db_table="charities"