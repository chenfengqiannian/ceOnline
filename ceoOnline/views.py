from django.shortcuts import render
from django.http import *
from .models import *
from datetime import *
from django.db import models
from .form import *
# Create your views here.
import json
def usertodict(muser):
    fields = muser._meta.get_all_field_names()
    userdict = {}
    for field in fields:

        if(field=='didian' or field=="renews_from" or field=="renews_to" or field=="refriend_from" or field=="refriend_to" ):
            continue
        if (field == 'onlinetime'):
            userdict['onlinetime'] = muser.onlinetime.strftime("%Y-%m-%d %H:%M:%S")

            continue
        if (type(getattr(muser, field)) is models.fields.files.ImageFieldFile):
            userdict[field] = getattr(muser, field).name
            continue

        userdict[field] = getattr(muser, field)
    return userdict


def ImageUpApi(request):
    try:
        if request.method == 'POST':
            form = AddForm(request.POST, request.FILES)
            if (form.is_valid()):
                imageData1 = form.cleaned_data['image1']
                imageData2 = form.cleaned_data['image2']
                imageData3 = form.cleaned_data['image3']
                imageData4 = form.cleaned_data['image4']
                imageData5 = form.cleaned_data['image5']
                touxingData=form.cleaned_data['touxiang']
            # mPhone='1'
            mPhone = request.POST['phone']

            mUser = user.objects.get(phone=mPhone)
            mUser.image1 = imageData1
            mUser.image2 = imageData2
            mUser.image3 = imageData3
            mUser.image4 = imageData4
            mUser.image5 = imageData5
            mUser.touxiang=touxingData
            mUser.save()
            return HttpResponse('ok')
        if request.method == 'GET':
            form = AddForm()

            return render(request, 'post.html', {'form': form})



    except Exception, e:
        print e
        return HttpResponseServerError(e)

def userinapi(request):
    try:
        if request.method == 'POST':

            data = json.loads(request.body)

            dataphone = data['phone']
            leixing = data.get('leixing', '-1')
            if (leixing == '0'):
                if (user.objects.get(phone=data['phone']).userpw == data['userpw']):
                    return HttpResponse("ok")
                else:
                    return HttpResponseForbidden()
            if (leixing == '1'):
                if (len(user.objects.filter(phone=data['phone'])) >= 1):
                    return HttpResponseForbidden()
                else:

                    myuser = user.objects.create(phone=data['phone'], password=data['password'],onlinetime=datetime.now())
                    myuser.dizhi=data['didian']
                    tb=tb_prov_city_area_street.objects.filter(name=data['didian'])
                    if(tb.count>=1):
                        myuser.didian=tb[0]

                    myuser.jianjie=data['jianjie']
                    myuser.zhiwu = data['zhiwu']
                    myuser.name = data['name']

                    myuser.save()


                    # myuser.didianchar.add(mydidian)
                    return HttpResponse('ok')
            if (leixing == '2'):
                userpwxiugai = user.objects.get(phone=data['phone'])
                if (userpwxiugai.userpw == data['olduserpw']):
                    userpwxiugai.userpw = data['newuserpw']
                    userpwxiugai.save()
                    return HttpResponse('ok')
                else:
                    return HttpResponseForbidden()


            clphone = user.objects.get(phone=dataphone)
            reqkey = data.keys()

            for k in reqkey:
                setattr(clphone, k, data[k])
            clphone.save()
            return HttpResponse("ok")
        if request.method=="GET":


            dataphone = request.GET.get('phone')
            muser=user.objects.get(phone=dataphone)


            usertdict=usertodict(muser)
            muser.onlinetime = datetime.now()
            muser.save()
            return JsonResponse(usertdict,safe=False)











    except Exception, e:
            print e
            return HttpResponseServerError(e)
def wenzisousuo(request):
    try:
        if request.method == 'GET':
            data = request.GET.get('data')
            muser=user.objects.filter(name__contains=data)

            userlist=[]
            for mu in muser:

                userlist.append(usertodict(mu))

            return JsonResponse(userlist,safe=False)


    except Exception, e:
            print e
            return HttpResponseServerError(e)
def shaixuan(request):
    try:
        if request.method == 'GET':
            code = request.GET.get('code',-1)
            if(code==-1):
                tb_set=tb_prov_city_area_street.objects.filter(level=1)

                shaixuandict = {}
                for i in tb_set:
                    shaixuandict[i.name]=i.code


                return JsonResponse(shaixuandict,safe=False)
            else:
                tb_set = tb_prov_city_area_street.objects.filter(parentId=code)
                if(tb_set.count()>=1):
                    shaixuandict = {}
                    for i in tb_set:
                        shaixuandict[i.name] = i.code

                    return JsonResponse(shaixuandict,safe=False)
                else:
                    tb=tb_prov_city_area_street.objects.get(code=code)
                    muser=tb.user_set.all()
                    userlist = []
                    for mu in muser:

                        userlist.append(usertodict(mu))
                    return JsonResponse(userlist,safe=False)










    except Exception, e:
            print e
            return HttpResponseServerError(e)
def friendapi(request):
    try:
        if request.method == 'GET':
            phone = request.GET.get('phone',-1)
            state=request.GET.get('state',-1)

            muser=user.objects.get(phone=phone)
            qs1=muser.refriend_from.all()
            qs2=muser.refriend_to.all()

            qs=qs1 |qs2

            if(state!=-1):
                qs=qs.filter(state=state)
            freindqs = qs.distinct()
            weidu=freindqs.filter(yidu=False).count()
            for du in qs:
                du.yidu=True
                du.save()

            friendlist = []
            for mu in freindqs:
                frienddict={}
                frienddict['createtime']=mu.createtime.strftime("%Y-%m-%d %H:%M:%S")
                frienddict['fromphone'] = mu.fromuser.phone
                frienddict['fromimage'] = mu.fromuser.touxiang.name
                frienddict['tophone'] = mu.touser.phone
                frienddict['toimage'] = mu.touser.touxiang.name
                frienddict['state'] = mu.touser.state

                friendlist.append(frienddict(mu))
            moutdict={}
            moutdict['weidu']=weidu
            moutdict['data']=friendlist
            return JsonResponse(moutdict, safe=False)
        if request.method == 'POST':
            data = json.loads(request.body)
            if(data.get('id',-1)!=-1):
                mf=friend.objects.get(id=data['id'])
                mf.state=data.get('state',0)
                mf.save()
                return HttpResponse("ok")


            dataphone = data['phone']
            tophone=data['tophone']
            state=data['state']
            fromuser=user.objects.get(phone=dataphone)
            touser=user.objects.get(phone=tophone)

            friend.objects.create(fromuser=fromuser,touser=touser,state=state)
            return HttpResponse('ok')

















    except Exception, e:
            print e
            return HttpResponseServerError(e)


def newsapi(request):
    try:
        if request.method == 'GET':
            phone = request.GET.get('phone', -1)


            muser = user.objects.get(phone=phone)
            qs1 = muser.renews_from.all()
            qs2 = muser.renews_to.all()

            qs = qs1 | qs2



            newsqs = qs.distinct()
            weidu = newsqs.filter(yidu=False).count()
            for du in qs:
                du.yidu = True
                du.save()



            userlist = []
            for mu in newsqs:
                newsdict = {}
                newsdict['createtime'] = mu.createtime.strftime("%Y-%m-%d %H:%M:%S")
                newsdict['fromphone']=mu.fromuser.phone
                newsdict['fromimage'] = mu.fromuser.touxiang.name
                newsdict['tophone'] = mu.touser.phone
                newsdict['toimage'] = mu.touser.touxiang.name
                newsdict['neirong']=mu.neirong
                userlist.append(newsdict)

            outdict = {}
            outdict['weidu'] = weidu
            outdict['data'] = userlist

            return JsonResponse(outdict, safe=False)
        if request.method == 'POST':
            data = json.loads(request.body)
            dataphone = data['phone']
            tophone = data['tophone']
            neirong = data['neirong']
            fromuser = user.objects.get(phone=dataphone)
            touser = user.objects.get(phone=tophone)

            news.objects.create(fromuser=fromuser, touser=touser, neirong=neirong)
            return HttpResponse('ok')

















    except Exception, e:
        print e
        return HttpResponseServerError(e)