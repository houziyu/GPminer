from django.db import models

# Create your models here.

class download_app_url(models.Model):
    #下载软件连接url
    name = models.CharField(u'软件版本名称',max_length=100)
    download_url = models.CharField(u'软件下载url',max_length=100)
    def __str__(self):
        return self.name

class course_image_parameter(models.Model):
    #图片教程参数
    title = models.CharField(u'标题',max_length=100)
    url = models.CharField(u'教程url',max_length=100)
    image = models.CharField(u'图片地址',max_length=100)
    content = models.CharField(u'简述内容',max_length=100)
    def __str__(self):
        return self.title

class about_us(models.Model):
    name = models.CharField(u'联系方法',max_length=100)
    content = models.CharField(u'联系内容',max_length=100)
    def __str__(self):
        return self.name


