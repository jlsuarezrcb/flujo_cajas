from django import forms

from apps.flujo.models import Activo


class FrmActivo(forms.ModelForm):
    class Meta:
        model = Activo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
