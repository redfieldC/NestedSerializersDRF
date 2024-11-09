from django.db import models
import uuid
# Create your models here.

class Color(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=20)
    description=models.TextField()


class Product(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=40)
    price=models.IntegerField()
    description=models.TextField()
    color=models.ForeignKey(Color,on_delete=models.CASCADE)