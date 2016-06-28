import logging
from django.shortcuts import render
from django.conf import settings

logger = logging.getLogger('blog.views')

def global_setting(request):
	return {'SITE_NAME' : settings.SITE_NAME,
			'SITE_DESC' : settings.SITE_DESC,
			'PRO_EMAIL' : settings.PRO_EMAIL}

# Create your views here.
def index(request):
	try:
		pass
	except Exception as e:
		pass
	return render(request, 'index.html', locals())