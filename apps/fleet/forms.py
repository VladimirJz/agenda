from .models import Event,FuelSupply
import floppyforms as forms
import floppyforms.__future__ as forms
from floppyforms import widgets


class NewEventForm(forms.ModelForm):

     class Meta:
        model = Event
        fields = ('__all__')


# generic event form
class EventForm(forms.ModelForm):
   class Meta:
      model=Event
      exclude = ['Type','Vehicle','created_by']
      #fields=('__all__')

# detailed event / activity form
class FuelSupplyForm(forms.ModelForm):
   class Meta:
      model=FuelSupply
      exclude=['Event']
      #fields=('__all__')

   