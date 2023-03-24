from .models import Appointment
class EventForm(forms.ModelForm):
   class Meta:
      model=Appointment
      fields=('__all__')