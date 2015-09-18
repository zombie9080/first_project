from django import template
import datetime
import hashlib
import re

register = template.Library()

# {% v | cut:"l" %}
@register.filter(name="cut")
def myCut(v,arg):
    return v.replace(arg,"*")

# {% v | md5 %}
@register.filter(name="md5")
def md5sum(v):
	md5 = hashlib.md5()		
	md5.update(v)
	return md5.hexdigest()


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

#{% start \d %}
@register.tag(name='start')
def start_level(parser,token):
	try:
		tag_name, level = token.split_contents()
		if re.match(r'\d',level):
			level = int(level)
		else:
			raise template.TemplateSyntaxError('syntax')
	except:
		raise template.TemplateSyntaxError('syntax')
	return StartNode(level)
class StartNode(template.Node):
	def __init__(self,level):
		self.level = level
	def render(self,context):
		fullstart = '*********'
		return fullstart[0:self.level]
	

		
