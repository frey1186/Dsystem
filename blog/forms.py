from django.forms import ModelForm
from blog.models import Comments


class CommentsModelForm(ModelForm):

    class Meta:
        model = Comments
        fields = ['vister','title','upper_comments','article','content']

    def __new__(cls, *args, **kwargs):

        for field_name in cls.base_fields:
            field = cls.base_fields[field_name]
            field.widget.attrs.update({"class": "form-control"})

        return ModelForm.__new__(cls)