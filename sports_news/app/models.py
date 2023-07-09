# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Matches(models.Model):
    name = models.CharField(max_length=50)
    tourid = models.ForeignKey('Tours', models.DO_NOTHING, db_column='tourId')  # Field name made lowercase.
    status = models.IntegerField()
    format = models.CharField(max_length=50)
    starttime = models.DateTimeField(db_column='startTime')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='endTime')  # Field name made lowercase.
    recupdatedat = models.DateTimeField(db_column='recUpdatedAt')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'matches'


class News(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    sportid = models.ForeignKey('Sports', models.DO_NOTHING, db_column='sportId')  # Field name made lowercase.
    tourid = models.ForeignKey('Tours', models.DO_NOTHING, db_column='tourId')  # Field name made lowercase.
    matchid = models.ForeignKey(Matches, models.DO_NOTHING, db_column='matchId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt', auto_now_add=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'news'


class Sports(models.Model):
    name = models.CharField(max_length=50)
    status = models.IntegerField()
    recupdatedat = models.DateTimeField(db_column='recUpdatedAt')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sports'


class Tours(models.Model):
    name = models.CharField(max_length=50)
    sportid = models.ForeignKey(Sports, models.DO_NOTHING, db_column='sportId')  # Field name made lowercase.
    status = models.IntegerField()
    starttime = models.DateTimeField(db_column='startTime')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='endTime')  # Field name made lowercase.
    recupdatedat = models.DateTimeField(db_column='recUpdatedAt')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tours'
