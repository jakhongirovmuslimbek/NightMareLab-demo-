from django.db import models
from django.contrib.auth import get_user_model

class RequestType(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

class Request(models.Model):
    user = models.ForeignKey(get_user_model(), related_name="requests", on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    body = models.TextField()
    type = models.ForeignKey(RequestType, related_name="requests", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
   
class Company(models.Model):
    model = models.FileField(upload_to="company/model/%y%m%d")
    logo = models.FileField(upload_to="company/logo/%y%m%d")
