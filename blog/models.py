from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

"""
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
"""

class Tracker(models.Model):
    mobile = PhoneNumberField() #using imported phone number resolution library
    quota = models.PositiveIntegerField()
    qtyTracked = models.PositiveIntegerField()
    def add(self):
        self.save()
    
    def __str__(self):
        return self.trackerMobile

class Trackee(models.Model):
    url = models.URLField()
    target = models.DecimalField(max_digits=11, decimal_places=2) #just under a billion
    last = models.DecimalField(max_digits=11, decimal_places=2, null=True) #just under a billion
    name = models.CharField(max_length=200, null=True)
    mobile = PhoneNumberField() #using imported phone number resolution library
    trackerCode = models.ForeignKey(Tracker, on_delete = models.CASCADE, null=True)   
    createdDate = models.DateTimeField(default=timezone.now)
    def add(self):
        self.save()
    
    def __str__(self):
        return self.url
