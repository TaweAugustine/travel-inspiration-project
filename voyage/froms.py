
from django.core.exceptions import ValidationError
from django import forms
from .models import TravelInspiration, Favorites
from django.contrib.auth.models import User

class TravelInspirationForm(forms.ModelForm):
   
    class Meta :
        model = TravelInspiration 
        fields = ('budget','travel_date_start','travel_date_end','prefered_activitties',)   
        
        widgets ={
            'budget' : forms.NumberInput(attrs={
                "class" : "form-control text-center",
                "placeholder" : "Entrez le budget prévue pour votre voyage "
            }),
            
            'travel_date_start' : forms.DateInput(attrs={
                "class" : "form-control text-center",
                "placeholder" : "Entrer la date de voyage "
            }),
            'travel_date_end' : forms.DateInput(attrs={
                "class" : "form-control text-center",
                "placeholder" : "Entrez la date de retour "
            }),
            
              'prefered_activitties' : forms.Textarea(attrs={
                "class" : "form-control text-center",
                "placeholder" : "Quelles sont vos activités préférées ? "
            })
        }
