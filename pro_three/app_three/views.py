from django.shortcuts import render
from django.http import HttpResponse
from app_three.models import Topic, AccessRecord,Webpage
# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by("date")
    date_dict = {"AccessRecord":webpages_list}
    #return HttpResponse("<em>My second App! Yepee- Include function worked!</em>")
    return render (request,"app_three/index.html", context=date_dict)
