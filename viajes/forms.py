from django import forms
from .models import Viaje

class ViajeForm(forms.ModelForm):
    class Meta:
        model = Viaje
        fields = ['destino', 'descripcion', 'fecha', 'kilometros', 'dificultad', 'guia', 'pilotos']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(ViajeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs['class'] = 'form-control'
        self.fields['pilotos'].widget.attrs['id'] = 'id_pilotos'