from .models import Event
import floppyforms as forms
import floppyforms.__future__ as forms
from floppyforms import widgets


class NewEventForm(forms.ModelForm):

     class Meta:
        model = Event
        fields = ('__all__')