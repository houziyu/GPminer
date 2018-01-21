# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-21 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_us',
            name='content',
            field=models.CharField(max_length=100, verbose_name='联系内容'),
        ),
        migrations.AlterField(
            model_name='about_us',
            name='name',
            field=models.CharField(max_length=100, verbose_name='联系方法'),
        ),
        migrations.AlterField(
            model_name='course_image_parameter',
            name='content',
            field=models.CharField(max_length=100, verbose_name='简述内容'),
        ),
        migrations.AlterField(
            model_name='course_image_parameter',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='图片上传'),
        ),
        migrations.AlterField(
            model_name='course_image_parameter',
            name='title',
            field=models.CharField(max_length=100, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='course_image_parameter',
            name='url',
            field=models.CharField(max_length=100, verbose_name='教程url'),
        ),
        migrations.AlterField(
            model_name='download_app_url',
            name='download_app_url',
            field=models.CharField(max_length=100, verbose_name='软件下载url'),
        ),
        migrations.AlterField(
            model_name='download_app_url',
            name='name',
            field=models.CharField(max_length=100, verbose_name='软件版本名称'),
        ),
    ]