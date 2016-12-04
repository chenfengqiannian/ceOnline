# -*- coding:utf-8 -*-


from django.db import models

# Create your models here.
class user(models.Model):
    phone=models.CharField(u'手机号',max_length=255)
    password=models.CharField(u'密码',max_length=255)
    jianjie = models.TextField(u'简介')
    zhiwu = models.CharField(u'职务', max_length=255,blank=True)
    dizhi=models.CharField(u'地址',max_length=255,blank=True)
    gongsi=models.CharField(u'公司',max_length=255,blank=True)
    name=models.CharField(u'名称',max_length=255,blank=True)
    touxiang = models.ImageField(u'头像',blank=True,upload_to='images')
    image1 = models.ImageField(u'图像1',blank=True,upload_to='images')
    image2 = models.ImageField(u'图像2',blank=True,upload_to='images')
    image3 = models.ImageField(u'图像3',blank=True,upload_to='images')
    image4 = models.ImageField(u'图像4',blank=True,upload_to='images')
    image5 = models.ImageField(u'图像5',blank=True,upload_to='images')
    isVIP=models.BooleanField(u'是否金色名称',default=False)
    bankuai=models.CharField(u'板块',max_length=255,default=u"免费版")
    onlinetime=models.DateTimeField()
    didian=models.ForeignKey('tb_prov_city_area_street',blank=True,null=True)
    def __unicode__(self):
        return self.phone
class setting(models.Model):
    name=models.CharField(u'名称',max_length=255)
    value=models.TextField(u'内容')
    def __unicode__(self):
        return self.name
class news(models.Model):
    fromuser=models.ForeignKey(user,related_name="renews_from")
    touser=models.ForeignKey(user,related_name="renews_to")
    neirong=models.TextField(u'内容')
    createtime = models.DateTimeField(auto_now_add=True)
    yidu=models.BooleanField(default=False)
    def __unicode__(self):
        return self.fromuser.name
class friend(models.Model):
    fromuser=models.ForeignKey(user,related_name="refriend_from")
    touser=models.ForeignKey(user,related_name="refriend_to")
    statechoice=((0,u'请求'),(1,u'好友'))
    yidu = models.BooleanField(default=False)
    state=models.IntegerField(choices=statechoice,default=0)
    createtime=models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.fromuser.name
class tb_prov_city_area_street(models.Model):
    code=models.IntegerField(blank=True)
    parentId=models.IntegerField(blank=True)
    name=models.CharField(max_length=50,blank=True)
    level=models.IntegerField(blank=True)
    def __unicode__(self):
        return self.name
