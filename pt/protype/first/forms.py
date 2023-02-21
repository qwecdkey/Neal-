from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Picture

class customizeRegistList(UserCreationForm):
    AuburnID = forms.CharField(required = False,max_length = 50)
    
    class Meat:
        model = User
        fields = ('AuburnID')
        
class pic_Form(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['title', 'picture']        