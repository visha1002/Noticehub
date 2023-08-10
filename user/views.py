from django.shortcuts import render
from myadmin.models import Notices
# Create your views here.

def index(request):
    allnotices = Notices.objects.all()
    context = {'result':allnotices}
    return render(request, 'index.html', context)