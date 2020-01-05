from django import forms
from .models import Image,Profile,Comments

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['editor', 'pub_date','profile','likes','comments','followers']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
class NewProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['editor']
        widgets={
            'tags':forms.CheckboxSelectMultiple(),
        }

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['editor']
        widgets={
            'tags':forms.CheckboxSelectMultiple(),
        }
        
class NewCommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        exclude=['editor']
      
       