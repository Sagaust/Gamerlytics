from django.db import models
from django.db.migrations.state import ModelState

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=2000)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)