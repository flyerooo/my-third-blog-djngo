import logging
from django.shortcuts import render

logger = logging.getLogger('blog.views')

# Create your views here.
def index(request):
	return render(request, 'index.html', locals())