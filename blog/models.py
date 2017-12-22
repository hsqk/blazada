from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

class Trackee(models.Model):
    url = models.URLField()
    target = models.DecimalField(max_digits=11, decimal_places=2) #just under a billion
    last = models.DecimalField(max_digits=11, decimal_places=2, null=True) #just under a billion
    name = models.CharField(max_length=200, null=True)
    mobile = PhoneNumberField() #using imported phone number resolution library
    createdDate = models.DateTimeField(default=timezone.now)
    def add(self):
        self.save()
    
    def __str__(self):
        return self.url
