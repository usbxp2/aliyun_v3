#-*- coding:utf-8 -*-
from django.shortcuts import render,render_to_response, redirect
from app.models import *
from django.http import HttpResponse
from django.template import RequestContext,loader
import datetime
import forms
# 邮件部分
from django.core.mail import EmailMessage
from settings import EMAIL_HOST_USER   #项目配置邮件地址，请参考发送普通邮件部分

#创建发送邮件的函数
def send_html_mail(subject, html_content, recipient_list):
    msg = EmailMessage(subject, html_content, EMAIL_HOST_USER, recipient_list)
    msg.content_subtype = "html" # Main content is now text/html
    msg.send()

# 邮件部分结束

def sendmail(request):
    #获取最近一个月有到期的业务的公司id列表
    startdate = datetime.datetime.now().date()
    enddate = startdate + datetime.timedelta(30)
    comname = Business.objects.filter(exp_date__range = (startdate,enddate))
    com_name_list = []
    for i in comname:
        com_name_list.append(i.com_name_id)
    #公司id列表中去年重复的
    com_name_list = list(set(com_name_list))
    print com_name_list
    list_email = []


    for id in com_name_list:   #遍历公司id列表
        com_info = Customer.objects.get(id=id)   #获取公司信息
        today = datetime.date.today()
        bus_info = Business.objects.filter(com_name_id=id,exp_date__gte=today)   #获取公司下所有业务信息

        #将每条业务的id和对应的价格放入字典
        pricedic={}
        for i in bus_info:  #遍历公司下所有业务
           pricedic[i.id] = Product.objects.get(id=i.pro_name_id).price  #往字典中追加数据
       
        #发送的html内容
        html_content = loader.render_to_string(
                           'app/mail_template.html',                                 #需要渲染的html模板
                               {
                                 'com_info':com_info,                   #参数
                                 'bus_info':bus_info,
                                 'pricedic':pricedic,
                               }
                           )
        subject = '万网业务续费通知'
        recipient_list = [com_info.email]  #收件人列表
        list_email.append(com_info.email + '      ' +com_info.com_name + '<br>')
        send_html_mail(subject,html_content,recipient_list)  #调用函数发送邮件
    return HttpResponse(list_email)

ONE_PAGE_OF_DATA = 50

def index(request):
    try:
        curPage = int(request.GET.get('curPage','1'))
	allPage = int(request.GET.get('allPage','1'))
	pageType = str(request.GET.get('pageType'))
    except ValueError:
	curPage = 1
	allPage = 1
	pageType = ''
		
    if pageType == 'pageDown':
	curPage += 1
    elif pageType == 'pageUp':
	curPage -= 1
		
    startPos = (curPage-1) * ONE_PAGE_OF_DATA
    endPos = startPos + ONE_PAGE_OF_DATA
    bus_list = Business.objects.all()[startPos:endPos]
    dep_list = {}
    for i in bus_list:
        id = Customer.objects.get(id=i.com_name_id).dep_name_id
        dep_list[i.id] = Department.objects.get(id=id).dep_name

    if curPage == 1 and allPage == 1:
	allPostCounts = Business.objects.count()
	allPage = allPostCounts / ONE_PAGE_OF_DATA
	remainPost = allPostCounts % ONE_PAGE_OF_DATA
	if remainPost > 0:
        	allPage += 1

    return render_to_response('app/index.html',{'bus_list':bus_list,'dep_list':dep_list,'allPage':allPage,'curPage':curPage})

def search(request, id=0):
    if request.method == 'POST':
        search_name = request.POST.get('search_name').strip()
    else:
        search_obj = Business.objects.get(id=id)
        search_name = search_obj.com_name.com_name

    bus_list = Business.objects.filter(com_name__com_name__contains = search_name)  #contains模糊查询,外键需要具体到外键表中的字段，用__（两个下划线）连接。
    dep_list = {}
    pri_list = {}
    for i in bus_list:
        pri_list[i.id] = Product.objects.get(id=i.pro_name_id).price
        dep_list[i.id] = Customer.objects.get(id=i.com_name_id).dep_name
    return render_to_response('app/search.html',{'bus_list':bus_list,'dep_list':dep_list,'pri_list':pri_list})

def update(request):
    buss_id = request.POST.get('buss_id')
    bus_this = Business.objects.get(id=buss_id)
    print bus_this.exp_date.year
    bus_this.exp_date = bus_this.exp_date.replace(year = bus_this.exp_date.year + 1)
    bus_this.save()
    print bus_this.exp_date
    #return HttpResponse('续费成功')
    return redirect('/xufei_search/%s' % buss_id)
    
def month(request):
    #获取最近一个月到期的业务列表
    startdate = datetime.datetime.now().date()
    enddate = startdate + datetime.timedelta(30)
    #查询一个月内到期的业务，filter就包含了order_by，默认是按照表id
    bus_list = Business.objects.filter(exp_date__range = (startdate,enddate))
    #按部门进行分组，即在排序的基础上按部门分组
    bus_list.query.group_by = ['com_name__dep_name_id']
    pri_list = {}
    dep_list = {}
    for i in bus_list:
        pri_list[i.id] = Product.objects.get(id=i.pro_name_id).price
        id = Customer.objects.get(id=i.com_name_id).dep_name_id
        dep_list[i.id] = Department.objects.get(id=id).dep_name
    return render_to_response('app/month.html',{'bus_list':bus_list,'pri_list':pri_list,'dep_list':dep_list})

def xufei(request):
    return render(request,'app/xufei.html')


def xufei_search(request, bus_id=0):
    if request.method == 'POST':
        search_name = request.POST.get('search_name')
    else:
        search_obj = Business.objects.get(id=bus_id)
        search_name = search_obj.com_name.com_name
    bus_list = Business.objects.filter(com_name__com_name__contains = search_name)  #contains模糊查询,外键需要具体到外键表中的字段，用__（两个下划线）连接。
    dep_list = {}
    for i in bus_list:
        dep_list[i.id] = Customer.objects.get(id=i.com_name_id).dep_name
    return render_to_response('app/xufei_search.html',{'bus_list':bus_list,'dep_list':dep_list})

def custom(request,custom_id):
    cus_list = Customer.objects.get(id=custom_id)
    return render_to_response('app/custom.html',{'cus_list':cus_list})

def overdue(request):
    bus_list = Business.objects.filter(exp_date__lte = datetime.date.today()).order_by('-exp_date')
    pri_list = {}
    dep_list = {}
    for i in bus_list:
        pri_list[i.id] = Product.objects.get(id=i.pro_name_id).price
        id = Customer.objects.get(id=i.com_name_id).dep_name_id
        dep_list[i.id] = Department.objects.get(id=id).dep_name
    return render_to_response('app/overdue.html',{'bus_list':bus_list,'pri_list':pri_list,'dep_list':dep_list})
 
def add_comment(request):
    if request.method == "POST":
        #提取form表单发来的数据
        bus_id = request.POST.get('bus_id')
        comment = request.POST.get('comment')
        url = request.POST.get('prov_url')
        #如果不为空，写数据库；其实这里如果用ajax与前台交互，会有更好的体验，我偷懒了。
        if comment.strip():
            try:
                Business.objects.filter(id=bus_id).update(comment=comment)
            except Exception as e:
                print(e)
        if 'search' in url:
            print "搜索跳转"
            return redirect('/search/%s' % bus_id)
        return redirect(url)