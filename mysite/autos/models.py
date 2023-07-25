from django.db import models

# Create your models here.

class Make(models.Model):
    name = models.CharField(max_length=128, default="")
    def __str__(self) :
        return self.name

class Auto(models.Model):
    nickname = models.CharField(max_length=300)
    mileage = models.IntegerField(null=True)
    comments = models.TextField(default = '')
    make = models.ForeignKey("Make", on_delete=models.CASCADE, null=True)