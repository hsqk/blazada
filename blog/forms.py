from django import forms

from .models import Trackee

from captcha.fields import ReCaptchaField

class TrackeeForm(forms.ModelForm):
    
    class Meta:
        model = Trackee
        fields = ('url', 'target', 'mobile')
    
#    captcha = ReCaptchaField()


