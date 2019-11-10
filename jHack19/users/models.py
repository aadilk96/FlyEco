from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    phone = models.TextField(default='+4917628596445')
    def __str__(self): 
        return "%s"%self.user.username

class Flight(models.Model): 
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    outbound = models.TextField()
    inbound = models.TextField()
    roundTrip = models.BooleanField()
    price = models.FloatField()
    emissions = models.FloatField()
    outboundDate = models.TextField()
    inboundDate = models.TextField()
    def __str__(self): 
        return "%s to %s at %s"%self.outbound, self.inbound, self.price