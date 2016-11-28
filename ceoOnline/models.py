# -*- coding:utf-8 -*-


from django.db import models

# Create your models here.
class user(models.Model):
    phone=models.CharField(u'手机号',max_length=255)
    password=models.CharField(u'密码',max_length=255)
    jianjie = models.TextField(u'简介')
    zhiwu = models.CharField(u'职务', max_length=255,blank=True)
    dizhi=models.CharField(u'地址',max_length=255,blank=True)
    touxiang = models.ImageField(u'头像',blank=True)
    image1 = models.ImageField(u'图像1',blank=True)
    image2 = models.ImageField(u'图像2',blank=True)
    image3 = models.ImageField(u'图像3',blank=True)
    image4 = models.ImageField(u'图像4',blank=True)
    image5 = models.ImageField(u'图像5',blank=True)
    isVIP=models.BooleanField(u'是否金色名称')
    bankuai=models.CharField(u'板块',max_length=255,blank=True)
    onlinetime=models.DateTimeField()
    didian=models.ForeignKey('tb_prov_city_area_street',blank=True,null=True)
class setting(models.Model):
    name=models.CharField(u'名称',max_length=255)
    value=models.TextField(u'内容')
class news(models.Model):
    fromuser=models.ForeignKey(user,related_name="renews_from")
    touser=models.ForeignKey(user,related_name="renews_to")
    value=models.TextField(u'内容')
    createtime = models.DateTimeField(auto_now=True)
class friend(models.Model):
    fromuser=models.ForeignKey(user,related_name="refriend_from")
    touser=models.ForeignKey(user,related_name="refriend_to")
    statechoice=((0,u'请求'),(1,u'好友'))
    state=models.IntegerField(choices=statechoice,default=0)
    createtime=models.DateTimeField(auto_now=True)
class tb_prov_city_area_street(models.Model):
    code=models.IntegerField(blank=True)
    parentId=models.IntegerField(blank=True)
    name=models.CharField(max_length=50,blank=True)
    level=models.IntegerField(blank=True)
