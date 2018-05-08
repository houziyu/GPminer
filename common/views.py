from django.shortcuts import render,redirect,HttpResponse
from common import models as common_models
import json,datetime,random,string
from django.core.mail import send_mail
from GPminer import settings
# Create your views here.

def index(request):
    download_app_url = common_models.download_app_url.objects.all()
    all_url = []
    for i in download_app_url:
        a_url = {}
        a_url['name'] = i.name
        a_url['download_url'] = i.download_url
        all_url.append(a_url)
    print('all_url',all_url)
    ###############################################
    all_about_method = common_models.about_us.objects.all()
    all_about=[]
    for i in all_about_method:
        a_about = {}
        a_about['name'] = i.name
        a_about['content'] = i.content
        all_about.append(a_about)
    print('all_about',all_about)
    ##############################################
    all_course_method = common_models.course_image_parameter.objects.all()
    all_course = []
    for i in all_course_method:
        a_course = {}
        a_course['title'] = i.title
        a_course['url'] = i.url
        a_course['image'] = i.image
        a_course['content'] = i.content
        all_course.append(a_course)
    print('all_course',all_course)
    return render(request, 'common/index.html',context={'all_url': all_url,'all_about':all_about,'all_course':all_course})

def user_signup(request):
    if request.method == 'GET':
        return render(request, 'common/signup.html')
    if request.method == 'POST':
        ret = {'code': '1200'}
        data = request.POST
        ret['result']= data
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        re_password = data.get('re_password')
        if password != re_password:
            ret['code'] ='1500'
            ret['type'] = 'password'
            ret['message'] = '输入密码有误'
            print('ret500:',ret)
            return HttpResponse(json.dumps(ret))
        elif common_models.user.objects.filter(email=email):
            ret['code'] = '1500'
            ret['type'] = 'email'
            ret['message'] = '此邮箱已被注册~'
            print('ret500:', ret)
            return HttpResponse(json.dumps(ret))
        else:
            activation_code =''.join(random.sample(string.ascii_letters + string.digits, 15))
            common_models.user.objects.create(username=username,email=email,password=password,activation_code=activation_code)
            email_message = settings.domain_name + '/activation?username='+username +'&activation_code='+activation_code
            print(email_message)
            send_mail('GPminer账号激活邮件', email_message, '18611819511@163.com',
                      [email], fail_silently=False)
            return HttpResponse(json.dumps(ret))

def activation(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        activation_code = request.GET.get('activation_code')
        common_models.user.objects.filter(username=username,activation_code=activation_code).update(user_status=0)
        return render(request, 'common/index.html')