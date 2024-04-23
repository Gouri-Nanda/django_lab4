from django.db import models

# Create your models here.
# tables that are being created 
#make migration and migrate command reads the updation done here
#wrt database

class Calculation(models.Model):
    principal = models.DecimalField(max_digits = 10, decimal_places = 2)
    rate = models.DecimalField(max_digits = 5, decimal_places = 2)
    time = models.IntegerField()
    result = models.DecimalField(max_digits = 10, decimal_places = 2,blank = True)
    timestamp = models.DateTimeField(auto_now_add=True)