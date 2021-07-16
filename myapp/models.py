from django.db import models

class Log(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    date = models.DateTimeField()

    def __str__(self):
        return self.title
