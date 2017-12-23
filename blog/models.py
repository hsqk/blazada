from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

class Tracker(models.Model):
    mobile = PhoneNumberField(unique=True) #using imported phone number resolution library
    chatId = models.CharField(max_length=20, null=True)
    
    
    def __str__(self):
        return str(self.mobile)



class Trackee(models.Model):
    url = models.URLField()
    target = models.DecimalField(max_digits=11, decimal_places=2) #just under a billion
    #last = models.DecimalField(max_digits=11, decimal_places=2, null=True) #just under a billion
    name = models.CharField(max_length=200, null=True)
    mobile = PhoneNumberField() #using imported phone number resolution library
    createdDate = models.DateTimeField(default=timezone.now)
    tracker = models.ForeignKey(Tracker, on_delete = models.CASCADE, null=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    
    def __str__(self):
        return self.url


