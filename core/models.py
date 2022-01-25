from django.db import models

class Note(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=25)
    text = models.CharField(max_length=25, default='')
    
    def __str__(self):
        return self.title