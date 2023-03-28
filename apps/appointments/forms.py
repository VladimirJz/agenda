from .models import Appointment
import floppyforms as forms
import floppyforms.__future__ as forms


class AppointmentForm(forms.ModelForm):
   class Meta:
      model=Appointment
      fields=('__all__')