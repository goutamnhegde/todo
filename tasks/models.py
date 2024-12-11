from django.db import models

class Tasks(models.Model):
    Title=models.CharField(max_length=260)
    

