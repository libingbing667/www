
import logging
from django.shortcuts import render
from django.conf import settings


logger = logging.getLogger('blog.views')
# Create your views here.

def global_setting(requet):   #调用settings
    return {'SITE_NAME': settings.SITE_NAME,   #把setting方法读取出来
            'SITE_DESC': settings.SITE_DESC    #返回定义的信息
            }


def index(request):
    return render(request,'index.html',locals())