#-*-coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aliyun_v3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sendmail/$','app.views.sendmail',name='sendmail'),
    url(r'^index/$','app.views.index',name='index'),  #给url取个名，在template里就可以用url标签来设置链接
    url(r'^search/$','app.views.search'),
    url(r"^search/(?P<id>\d+)/$", 'app.views.search', name='search'),
    url(r'^update/$','app.views.update'),
    url(r'^month/$','app.views.month',name='month'),
    url(r'^overdue/$','app.views.overdue',name='overdue'),
    url(r"^xufei/$",'app.views.xufei'),
    url(r"^xufei_search/$",'app.views.xufei_search'),
    url(r"^custom/(?P<custom_id>\d+)/$",'app.views.custom',name='custom'),
    url(r"^xufei_search/(?P<bus_id>\d+)/$", 'app.views.xufei_search'),
    url(r"^add_comment/$", 'app.views.add_comment', name="add_comment"),
)
