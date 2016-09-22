#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.

class Product(models.Model):
    pro_name = models.CharField(max_length=50,verbose_name='产品名称')
    cost = models.DecimalField(max_digits=7, decimal_places=2,default=0, verbose_name='成本(元/年)')
    price = models.DecimalField(max_digits=7,decimal_places=2,verbose_name='产品价格(元/年)')

    def __unicode__(self):
        return self.pro_name

    class Meta():
        verbose_name = '产品管理'
        verbose_name_plural = '产品管理'


class Department(models.Model):
    dep_name = models.CharField(max_length=50,verbose_name='部门名称')

    def __unicode__(self):
        return self.dep_name

    class Meta():
        verbose_name = '部门管理'
        verbose_name_plural = '部门管理'

class Customer(models.Model):
    com_name = models.CharField(max_length=100,verbose_name='公司名称')
    con_name = models.CharField(max_length=20,verbose_name='联系人姓名')
    tel = models.CharField(max_length=20,verbose_name='联系电话')
    email = models.EmailField(verbose_name='邮箱')
    dep_name = models.ForeignKey('Department',verbose_name='所属部门')

    def __unicode__(self):
        return self.com_name

    class Meta():
        verbose_name = '客户管理'
        verbose_name_plural = '客户管理'

class Business(models.Model):
    com_name = models.ForeignKey('Customer',verbose_name='公司名称')
    pro_name = models.ForeignKey('Product',verbose_name='产品名称')
    identify = models.CharField(max_length=200,verbose_name='绑定域名')
    host_name = models.CharField(max_length=200,default='null')
    exp_date = models.DateField(verbose_name="到期日期")
    comment = models.CharField(verbose_name="备注",default="", max_length=200)

    def __unicode__(self):
        return self.com_name.com_name

    class Meta():
        verbose_name = "业务管理"
        verbose_name_plural = "业务管理"
