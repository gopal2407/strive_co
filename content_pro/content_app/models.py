from django.db import models


# Create your models here.
class Content(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    context = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
