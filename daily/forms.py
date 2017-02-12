from django import forms
from django.forms import ModelForm
from daily import models



class DailyModelForm(ModelForm):
    class Meta:
        model = models.Daily
        fields = ['content','categories','hours']

    def __new__(cls, *args, **kwargs):

        for field_name in cls.base_fields:
            field = cls.base_fields[field_name]
            field.widget.attrs.update({"class": "form-control"})

        return forms.ModelForm.__new__(cls)

