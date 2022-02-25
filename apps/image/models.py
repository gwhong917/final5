from django.db import models
from django.conf import settings


class Post(models.Model):
     user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, db_column='user')
     model_pic = models.ImageField(upload_to='image/%Y/%m/%d')
     lat = models.FloatField(blank=True, null=True)
     lng = models.FloatField(blank=True, null=True)
     time = models.DateTimeField(auto_now_add=True)


