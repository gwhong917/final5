# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User


class Park(models.Model):
    t_id = models.AutoField(db_column='id', primary_key=True)
    t_name = models.CharField(db_column='name', max_length=50)
    t_type = models.TextField(db_column='type')
    t_job = models.CharField(db_column='job', max_length=50)
    t_age = models.IntegerField(db_column='age')

    #name = models.TextField()
    #type = models.ForeignKey(User, models.DO_NOTHING, db_column='draft_user')
    #job = models.DateTimeField(blank=True, null=True)
    #age = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'rest_api_test_kakaofriends'
        managed = False

    def __str__(self):
        return "제목 : " + self.name + ", 유형 : " + self.type

