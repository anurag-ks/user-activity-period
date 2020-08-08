from django.db import models


class UserModel(models.Model):
    '''
        UserModel - For user related information.
    '''
    id = models.CharField('ID', max_length=200, primary_key=True)
    real_name = models.CharField("Real Name", max_length=200)
    time_zone = models.CharField("Time Zone", max_length=200)


class ActivityPeriodModel(models.Model):
    '''
        ActivityPeriodModel - One-to-One relationship with UserModel. Stores start_time and end_time for the user.
    '''
    user = models.ForeignKey('UserModel', on_delete=models.CASCADE, verbose_name="user")
    start_time = models.DateTimeField("Start Time")
    end_time = models.DateTimeField("End Time")
