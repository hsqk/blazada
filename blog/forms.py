from django import forms

from .models import Trackee

from captcha.fields import ReCaptchaField

class TrackeeForm(forms.ModelForm):
    
    class Meta:
        model = Trackee
        fields = ('url', 'target', 'mobile')
        widgets = {
            'url': forms.URLInput(attrs={'placeholder': 'e.g. https://www.lazada.sg/xiaomi-redmi-4x-3gb-32gb-gold-20499139.html?spm=a2o42.prod.0.0.18feea70Ul1BP0', 'title':'Copy and paste from product page'}),
            'target': forms.NumberInput(attrs={'placeholder': 'e.g. 180', 'title': 'Exclude $ sign'}),
            'mobile': forms.TextInput(attrs={'placeholder': 'e.g. +65 96987636', 'title': 'Include + sign, country code'})
            }
    captcha = ReCaptchaField()


