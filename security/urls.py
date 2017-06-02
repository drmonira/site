from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^main/$',views.mainlogin_view,name="main_page_logtrick"),
    url(r'^$',views.log_reg,name="log_reg"),
    url(r'^authlog/$',views.user_auth_view,name="authinticate_login"),
    url(r'^reglog/$',views.user_reg_view,name="register_login"),
        url(r'^logout/$',views.logout_view,name="logout"),

]
