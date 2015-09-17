from django import template
import datetime

register = template.Library()

@register.filter(name="cut")
def myCut(v,arg):
    return v.replace(arg,"*")

#{% current_time "%Y-%m-%d %H:%M:%S" %}
@register.tag(name='current_time')
def do_current_time(parser,token):
    try:
        tag_name, format_string = token.split_contents()
    except:
        raise template.TemplateSyntaxError('syntax')
    return CurrentNode(format_string[1:-1])
class CurrentNode(template.Node):
    def __init__(self,format):
        self.format_string = str(format)
    def render(self,context):
        now = datetime.datetime.now()
        return now.strftime(self.format_string)
