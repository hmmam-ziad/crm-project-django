from django.db import models

# Create your models here.
# Category Model
class Category(models.Model):
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

# Client Model
class Record(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone = models.IntegerField()
    tall = models.IntegerField()
    wedigth = models.IntegerField()
    address = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    
