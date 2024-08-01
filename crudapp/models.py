from django.db import models

class Record(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=80)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name + " " + self.last_name

# Create your models here.
