from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.conf.urls.static import static
from django.conf import settings

from jdemo import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),

    # url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    # url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login'),
    # url(r'^accounts/profile/$', views.profile_view),

    url(r'^index$', views.index),
    url(r'^jconf$', views.jconf_view),
    url(r'^jcourse$', views.jcourse_view),
    url(r'^hipaa$', views.hipaa_view),
    url(r'^about$', views.about_view),
)
