from django.shortcuts import get_object_or_404, render,Http404,HttpResponse, redirect
from .forms import QueryForm,UploadFileForm
import pymysql
import os
from django.views.decorators.cache import cache_control

from django.utils import timezone
from django.template import loader
from .models import fw,sw
from django.db.models import Q
from django.db.models import F
#from .forms import ModelFormWithFileField

# Create your views here.


def clean_none(self,pdata): #处理post提交的none数据函数
    #pdata = self.cleaned_data['pdata']
    if pdata is None:
        return self.initial.get('pdata', 0)
    return pdata


def get_data(sql): #连接数据库，执行sql语句，获取数据库的数据
    #try:
    #except
    conn = pymysql.connect(host='127.0.0.1',user ='root',passwd='zhangjian',db='DjangoDB',port=3306,charset="utf8")
    cur = conn.cursor()
    cur.execute(sql)
    results = cur.fetchall()  # 搜取所有结果
    cur.close()
    conn.close()
    return results

def index(request,): # 向web页面输出所有产品信息
    sql = "SELECT * FROM `tableQuery_fw` WHERE 1"
    m_data = get_data(sql)
    return render(request,'tableQuery/index.html',{'latest_post':m_data})

def sforms(request):  #专用查询表单
    if request.method == 'GET':
        formdata = QueryForm()
        return render(request,'tableQuery/bootstrap4.html',{'formdata':formdata})
    else:
        formdata = QueryForm(request.POST)
        if formdata.is_valid():
            return HttpResponse('提交成功')
        return render(request,'tableQuery/bootstrap4.html',{'formdata':formdata})

@cache_control(private=True)
def fwsearch(request):# 向web页面输出查询结果
    f = QueryForm(request.POST)  #默认request.POST为空，当提交请求时，f中就带了提交的信息，返回页面。
    if request.method == "POST":  #这里POST一定要大写
        if f.is_valid():    #验证请求的内容和QueryForm里面的是否验证通过。通过是True，否则False。
            post_data = f.cleaned_data  #cleaned_data类型是字典，用户提交的数据可以和查询结果同时显示出来
            #rj45 = f.cleaned_data.get('rj45')
            #sfp = f.cleaned_data.get('ge_sfp')
            #thp = f.cleaned_data.get('thp')
            rj45 = f.cleaned_data['rj45']
            rj45 = clean_none(f,rj45)

            sfp = f.cleaned_data['ge_sfp']
            sfp = clean_none(f,sfp)

            g10c =f.cleaned_data.get('g10c')
            g10c = clean_none(f,g10c)

            sfpp = f.cleaned_data.get('sfpp')
            sfpp = clean_none(f,sfpp)

            g25 =f.cleaned_data.get('g25')
            g25 = clean_none(f,g25)

            qsfpp = f.cleaned_data.get('qsfpp')
            qsfpp = clean_none(f,qsfpp)

            cfp =f.cleaned_data.get('cfp')
            cfp = clean_none(f,cfp)

            slot =f.cleaned_data.get('slot')
            slot =clean_none(f,slot)    #业务插槽数量

            thp = f.cleaned_data.get('thp')
            thp  = clean_none(f,thp)    #交换性能

            ccs = f.cleaned_data.get('ccs')
            ccs = clean_none(f,ccs)   #转发性能

            nss = f.cleaned_data['nss']
            nss = clean_none(f,nss)
            #print(nss)


            #sql_result = "SELECT * FROM `tableQuery_fw` WHERE GE_RJ45>=%d AND GE_SFP>=%d AND Throughput>=%f " % (rj45,sfp,thp)
            #QT = get_data(sql_result)[:10]

            #根据提交的条件查询出所有符合条件的产品 QT
            QT = fw.objects.filter(GE_RJ45__gte=rj45, GE_SFP__gte=sfp,Cop_10GE__gte=g10c,SFPP_10GE__gte=sfpp,
                                   QSFPP_40GE__gte=qsfpp,CFP2_QSFP28_100GE__gte=cfp,Interface_Module_Slots__gte=slot,
                                   Throughput__gte=thp,Concurrent_Sessions__gte=ccs,New_Sessions_Sec__gte=nss)\
                                    .order_by('Vendors','Throughput')

            #distinct()  与mysql兼容不好，无法使用，需要自定义函数实现每个厂商筛选1～2款产品。  .values('Vendors').distinct()
            #print (str(fw.objects.filter(GE_RJ45=rj45).query))
            #print(QT.count())
            #print(QT[1].Vendors)



            #根据查询出来的产品QT，再针对每个厂商筛选1款产品显示处理。
            flag = ""
            list = []   #每个厂商筛选1款产品放入list
            for i in range(len(QT)):
                item = QT[i]
                if flag == item.Vendors:
                    continue
                elif flag=="" or flag!=item.Vendors:
                    flag = item.Vendors
                    list.append(item)
            #print(list)
            #根据条件查询出来的QT产品，再针对每个厂商筛选1款产品显示处理。
            return render(request,'tableQuery/bootstrap4.html',{'pd':list,'post_data':post_data})
        else:       #提交的数据没有验证通过时（是否符合forms的规则）
            f = QueryForm(request.POST)  # 默认request.POST为空，当提交请求时，f中就带了提交的信息，返回页面。
            data_error = f.errors
            return render(request,'tableQuery/bootstrap4.html', {'pd': f, 'Post_error': data_error})
    else:
        f = QueryForm()
        return render(request,'tableQuery/bootstrap4.html', {'pd': f})

def swsc(request):

    if request.method == 'GET':
        f = QueryForm()
        return render(request, 'tableQuery/swsc.html', {'PD':f})
    else:
        f = QueryForm(request.POST)

        if f.is_valid():
            post_data = f.cleaned_data  # cleaned_data类型是字典，用户提交的数据可以和查询结果同时显示出来
            #rj45 = f.cleaned_data['rj45']
            #sfp = f.cleaned_data['sfpge']
            #g10c = f.cleaned_data['g10c']
            #sfpp = f.cleaned_data['sfpp']
            #g25 =f.cleaned_data['g25']
            #qsfpp =f.cleaned_data['qsfpp']
            #cfp =f.cleaned_data['cfp']

            rj45 =f.cleaned_data.get('rj45')
            rj45 = clean_none(f,rj45)  #clean_none自定义函数，是处理提交的空数据None的，sql查询不允许None数据类型

            sfp = f.cleaned_data.get('ge_sfp')
            sfp = clean_none(f,sfp)

            g10c =f.cleaned_data.get('g10c')
            g10c = clean_none(f,g10c)

            sfpp = f.cleaned_data.get('sfpp')
            sfpp = clean_none(f,sfpp)

            g25 =f.cleaned_data.get('g25')
            g25 = clean_none(f,g25)

            qsfpp = f.cleaned_data.get('qsfpp')
            qsfpp = clean_none(f,qsfpp)

            cfp =f.cleaned_data.get('cfp')
            cfp = clean_none(f,cfp)

            slot =f.cleaned_data.get('slot')
            slot =clean_none(f,slot)    #业务插槽数量

            thp = f.cleaned_data.get('thp')
            thp  = clean_none(f,thp)    #交换性能

            fc = f.cleaned_data.get('fc')
            fc = clean_none(f,fc)   #转发性能

            swpd = sw.objects.filter(ge_port_chasis__gte=rj45,sfp_port_chasis__gte=sfp,g10_port_chasis__gte=g10c,
                                     sfpp_port_chasis__gte=sfpp,g25_port__gte=g25,g40_port__gte=qsfpp,
                                     g100_port__gte=cfp,io_slots__gte=slot,switching_capacity__gte=thp,
                                     ipv4_forwarding_performance_pps__gte=fc).order_by('vendors','switching_capacity')


            #根据查询出来的产品swpd，再针对每个厂商筛选1款产品显示处理。
            flag = ""
            list = []   #每个厂商筛选1款产品放入list
            for i in range(len(swpd)):
                item = swpd[i]
                if flag == item.vendors:
                    continue
                elif flag=="" or flag!=item.vendors:
                    flag = item.vendors
                    list.append(item)
            #print(list)
            #根据条件查询出来的QT产品，再针对每个厂商筛选1款产品显示处理。

        return render(request,'tableQuery/swsc.html', {'PD': list,'post_data':post_data})
        #else   如果没有验证通过...


def upload(request):
    if request.method == "POST":
        handle_upload_file(request.FILES['file'], str(request.FILES['file']))
        return HttpResponse('Successful')  # 此处简单返回一个成功的消息，在实际应用中可以返回到指定的页面中
    return render(request,'tableQuery/upload.html')


def handle_upload_file(file, filename):
    path = '/uploads/'  # 上传文件的保存路径，可以自己指定任意的路径
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path + filename, 'wb+')as destination:
        for chunk in file.chunks():
            destination.write(chunk)

