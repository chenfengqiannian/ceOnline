
from django import forms
 
class AddForm(forms.Form):
    touxiang=forms.ImageField()
    image1=forms.ImageField()
    image2 = forms.ImageField()
    image3 = forms.ImageField()
    image4 = forms.ImageField()
    image5 = forms.ImageField()