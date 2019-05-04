from django.conf.urls import include, url
from django.contrib import admin
from QualityManager import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'TestQualityManager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/',views.login)
]
