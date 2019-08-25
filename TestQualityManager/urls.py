from django.conf.urls import include, url
from django.contrib import admin
from QualityManager import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/',views.login),
    url(r'^reg/',views.reg),
    url(r'^index/',views.index),
    url(r'^login_out/',views.logout),

]
