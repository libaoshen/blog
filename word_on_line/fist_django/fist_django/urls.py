"""fist_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from learn import views

# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^add/(\d{1,2})/(\d{1,2})$', views.add),
#     url(r'^showUserInfo/(\d{1,3})$', views.showUserInfo),
#     url(r'^showUserInfo2/(\d{1,3})$', views.showUserInfo2),
#     url(r'^getEmByName/(.*)$', views.getEmployeeByName),
#     url(r'^getAllEm$', views.getAllEmployee),
#     url(r'^saveEm$', views.insertEmployee),
#     url(r'^getOne/(.*)$', views.getOne),
#     url(r'^search$', views.searchEm),
#     url(r'^search2$', views.searchEm2)
# ]

# use patterns
# urlpatterns = patterns('',
#                        (r'^admin/', include(admin.site.urls)),
#                        (r'^add/(\d{1,2})/(\d{1,2})$', views.add),
#                        (r'^showUserInfo/(\d{1,3})$', views.showUserInfo),
#                        (r'^showUserInfo2/(\d{1,3})$', views.showUserInfo2),
#                        (r'^getEmByName/(.*)$', views.getEmployeeByName),
#                        (r'^getAllEm$', views.getAllEmployee),
#                        (r'^saveEm$', views.insertEmployee),
#                        (r'^getOne/(.*)$', views.getOne),
#                        (r'^search$', views.searchEm),
#                        (r'^search2$', views.searchEm2)
#                     )

# use string describe view
# urlpatterns = patterns('',
#                        (r'^add/(\d{1,2})/(\d{1,2})$', 'learn.views.add'),
#                        (r'^showUserInfo/(\d{1,3})$', 'learn.views.showUserInfo'),
#                        (r'^showUserInfo2/(\d{1,3})$', 'learn.views.showUserInfo2'),
#                        (r'^getEmByName/(.*)$', 'learn.views.getEmployeeByName'),
#                        (r'^getAllEm$', 'learn.views.getAllEmployee'),
#                        (r'^saveEm$', 'learn.views.insertEmployee'),
#                        (r'^getOne/(.*)$', 'learn.views.getOne'),
#                        (r'^search$', 'learn.views.searchEm'),
#                        (r'^search2$', 'learn.views.searchEm2')
#                     )

# use common prefix string
# urlpatterns = patterns('learn.views',
#                        (r'^add/(\d{1,2})/(\d{1,2})$', 'add'),
#                        (r'^showUserInfo/(\d{1,3})$', 'showUserInfo'),
#                        (r'^showUserInfo2/(\d{1,3})$', 'showUserInfo2'),
#                        (r'^getEmByName/(.*)$', 'getEmployeeByName'),
#                        (r'^getAllEm$', 'getAllEmployee'),
#                        (r'^saveEm$', 'insertEmployee'),
#                        (r'^getOne/(.*)$', 'getOne'),
#                        (r'^search$', 'searchEm'),
#                        (r'^search2$', 'searchEm2')
#                     )

# use multiply common prefix string
urlpatterns = patterns('learn.views',
                       (r'^add/(?P<b>\d{1,2})/(?P<a>\d{1,2})$', 'add'),
                       (r'^showUserInfo/(\d{1,3})$', 'showUserInfo'),
                       (r'^showUserInfo2/(\d{1,3})$', 'showUserInfo2'),
                       (r'^getEmByName/(.*)$', 'getEmployeeByName'),
                       (r'^getAllEm$', 'getAllEmployee'),
                       (r'^saveEm$', 'insertEmployee'),
                       (r'^getOne/(.*)$', 'getOne'),
                       (r'^search$', 'searchEm'),
                       (r'^search2$', 'searchEm2')
                    )

urlpatterns += [url(r'^admin/', include(admin.site.urls)),]