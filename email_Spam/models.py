from __future__ import unicode_literals

from django.db import models

class Email(models.Model):
    email_text = models.CharField(max_length=500)
    email_id = models.IntegerField()
    email_date = models.DateTimeField('email date')

class Email_new(models.Model):
    email_filtered = models.ForeignKey(Email, on_delete=models.CASCADE)
    email_id_filtered = models.IntegerField()
    email_date_new = models.DateTimeField('email date')


# Create your models here.
