from django.db import models

# Create your models here.
class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    no_of_guests = models.PositiveIntegerField()
    booking_date = models.DateField()
    
class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveBigIntegerField()
    
    def __str__(self):
        return f'{self.title} : {str(self.price)}' 