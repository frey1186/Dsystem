import markdown
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()  # 自定义filter时必须加上


@register.filter(is_safe=True)  # 注册template filter
@stringfilter  # 希望字符串作为参数
def custom_first_char(value):

    try:
        ret = value.upper()[0]
    except:
        ret = '!'
    return ret