from django.db import models
from datetime import date

class Tasks(models.Model):
    Title=models.CharField(max_length=260)
    Completed=models.BooleanField(default=False)
    Date=models.DateField(default=date.today)

    def __str__(self):
        return f"{self.Title} and {self.Date} and {self.Completed}"

    

