
from django.forms.models import ModelForm
from django.forms import ValidationError
from django import forms
from pact.models import Pact, Buddy, Checkin


class PactForm(ModelForm):
    class Meta:
        model = Pact
        exclude = ['goal',]
     

class BuddyRequestForm(ModelForm):
    class Meta:
        model = Buddy
        fields = ['user', 'email',]
        
    def clean(self):
        cleaned_data = super(BuddyRequestForm, self).clean()
        user = cleaned_data.get("user")
        email = cleaned_data.get("email")
            
        if not user and not email:
            raise ValidationError( "Please fill out user or email")
            
        
class BuddyStatusForm(ModelForm):
    class Meta:
        model = Buddy
        fields = ['status',]

