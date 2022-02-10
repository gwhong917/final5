from django.db import models


class Post(models.Model):
    model_pic = models.ImageField(upload_to='image/%Y/%m/%d')
