from django.db import models
from accounts.models import Account

# Create your models here.
 
class  University(models.Model):
    user = models.ForeignKey(Account,verbose_name = "University Admin", on_delete= models.CASCADE)
    university_full_name = models.CharField(max_length=255, verbose_name="University full name",null = False, blank = False)
    university_name_abb = models.CharField(max_length=15, verbose_name="University full name",null = False, blank = False)
    date_added = models.DateTimeField(verbose_name="Added date", auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name="Date updated", auto_now=True)



    def __str__(self):
        return self.university_full_name
    


