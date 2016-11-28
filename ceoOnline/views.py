from django.shortcuts import render
from django.http import *
from .models import *
# Create your views here.
import json
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

                    myuser = user.objects.create(phone=data['phone'], userpw=data['userpw'])

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
    except Exception, e:
            print e
            return HttpResponseServerError(e)