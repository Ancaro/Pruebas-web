from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime
from django.template.loader import get_template
from django.template import Context
"""from djago.shortcuts import render_to_response"""

def hora_actual (request):
	ahora = datetime.now()
	d = {'nombre':'Andres','edad':26,'profesion':'CodeWorks','hora':ahora}
	t = get_template("hora.html")
	c = Context(d)
	html = t.render(c)
	return HttpResponse(html)

"""Definicion usando django
def hora_actual(request):
	ahora = datetime.now()
	d = {'nombre':'Camilo','edad':26,'profesion':'CodeWorks','hora':ahora}
	return render_to_response('hora.html',d
"""