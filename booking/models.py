from django.db import models
BASE_PRICE = 80.00
SUITE_UPCHARGE = 0.25
OCEAN_UPCHARGE = 0.25

# Create your models here.
class Room(models.Model):
    room_num = models.IntegerField(default=0)
    price = models.FloatField(default=BASE_PRICE)
    occupied = models.BooleanField(default=False)
    oceanside = models.BooleanField(default=False)
    suite = models.BooleanField(default=False)

    def __str__(self):
        return "Room #" + str(self.room_num)