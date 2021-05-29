from django.db import models


class Profile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    address = models.CharField(max_length=256)


class Posts(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    text = models.TextField()
