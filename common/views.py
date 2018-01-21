from django.shortcuts import render,redirect,HttpResponse
from common import models
# Create your views here.

def index(request):
    download_app_url = models.download_app_url.objects.all()
    all_url = []
    for i in download_app_url:
        a_url = {}
        a_url['name'] = i.name
        a_url['download_url'] = i.download_url
        all_url.append(a_url)
    print(all_url)
    ###############################################
    all_about_method = models.about_us.objects.all()
    all_about=[]
    for i in all_about_method:
        a_about = {}
        a_about['name'] = i.name
        a_about['content'] = i.content
        all_about.append(a_about)
    print(all_about)
    ##############################################
    all_course_method = models.course_image_parameter.objects.all()
    all_course = []
    for i in all_course_method:
        a_course = {}
        a_course['title'] = i.title
        a_course['url'] = i.url
        a_course['image'] = i.image
        a_course['content'] = i.content
        all_course.append(a_course)
    print(all_course)
    return render(request, 'common/index.html',context={'all_url': all_url,'all_about':all_about,'all_course':all_course})