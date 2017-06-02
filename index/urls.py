from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$',views.index_view,name="main"),
    url(r'^logreg/$',views.log_reg,name="log_reg"),
    url(r'^content/$',views.content_view,name="content"),
    url(r'^main/$',views.mainlogin_view,name="main_page_logtrick"),
     url(r'^more/$',views.more_view,name="more"),
]
