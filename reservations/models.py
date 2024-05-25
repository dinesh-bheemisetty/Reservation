# models.py
from django.db import models
from django.contrib.auth.models import User
import uuid

class Train(models.Model):
    train_number = models.CharField(max_length=10)
    train_name = models.CharField(max_length=100)

    def __str__(self):
        return self.train_name

class Reservation(models.Model):
    places_list= [('AKP','Anakapalli'),('VSKP', 'visakhapatnam'),('VJW', 'Vijayawada'), ('SEC','Secundrabad')]
    class_type =  [
        ('1A', 'First AC'),
        ('2A', 'Second AC'),
        ('3A', 'Third AC'),
        ('SL', 'Sleeper'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    class_type = models.CharField(max_length=50, choices=class_type)
    date_of_journey = models.DateField()
    from_place = models.CharField(max_length=100, choices=places_list)
    to_place = models.CharField(max_length=100, choices=places_list)
    pnr_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f'Reservation {self.pnr_number} by {self.user.username}'
