from django import forms

from .models import Tracker, Trackee

'''
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
'''

class TrackerForm(forms.ModelForm):
    
    class Meta:
        model = Tracker
        fields = ('mobile',)

class TrackeeForm(forms.ModelForm):
    
    class Meta:
        model = Trackee
        fields = ('url', 'target', 'mobile')
'''
class SaleForm(forms.ModelForm):
    
    class Meta:
        model = Clothes
        fields = ('item_code',)

class SettlementForm(forms.ModelForm):
    
    class Meta:
        model = Seller
        fields = ('seller_code',)
'''
