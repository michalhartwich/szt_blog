from django.conf.urls import url

from . import views

app_name = 'pages'

urlpatterns = [
    url(r'^$', views.HomepageView.as_view(), name='homepage'),
    url(r'^(?P<slug>[\w-]+)/*$', views.ShowView.as_view(), name='show'),
]
