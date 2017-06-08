from django.conf.urls import url, include
from . import views

urlpatterns = [
    #url(r'^$',views.content_view,name="content"),
    url(r'^$',views.contentnew_view,name="content"),
    url(r'^(?P<lesson_id>[0-9]+)/$',views.content_details_view,name="content_details"),
                
    
]
