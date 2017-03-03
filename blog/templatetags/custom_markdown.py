import markdown
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe
from markdown.extensions.headerid import HeaderIdExtension


register = template.Library()  # 自定义filter时必须加上


@register.filter(is_safe=True)  # 注册template filter
@stringfilter  # 希望字符串作为参数
def custom_markdown(value):
    return mark_safe(markdown.markdown(
        value,
        extensions=['markdown.extensions.fenced_code',   # 解析代码块 ```
                   'markdown.extensions.codehilite',    # 代码高亮
                   'markdown.extensions.tables',        # 解析表格
                   'markdown.extensions.toc',        # 解析目录
                   'markdown.extensions.attr_list',        # 添加class 列表
                   HeaderIdExtension(level=2), # 从h2开始解析
                   ],
        safe_mode=True,
        enable_attributes=False))