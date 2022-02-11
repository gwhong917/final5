from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.CharField(db_column='user', max_length=50)
    lat = models.FloatField(db_column='lat', max_length=50)
    lng = models.FloatField(db_column='lng', max_length=50)
    time = models.DateTimeField(db_column='time')
    model_pic = models.CharField(db_column='model_pic', max_length=200)
    #name = models.TextField()
    #type = models.ForeignKey(User, models.DO_NOTHING, db_column='draft_user')
    #job = models.DateTimeField(blank=True, null=True)
    #age = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'image_post'
        managed = False

    def __str__(self):
        return "제목 : " + self.name + ", 유형 : " + self.type



