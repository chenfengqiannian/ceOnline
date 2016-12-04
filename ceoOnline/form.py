
from django import forms
 
class AddForm(forms.Form):
    touxiang=forms.ImageField(required=False)
    image1=forms.ImageField(required=False)
    image2 = forms.ImageField(required=False)
    image3 = forms.ImageField(required=False)
    image4 = forms.ImageField(required=False)
    image5 = forms.ImageField(required=False)