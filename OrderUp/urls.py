from django.conf.urls import url , include
from django.contrib.auth import views as auth_views
from OrderUp import views as OrderUp_views

urlpatterns = [
    url(r'^$',OrderUp_views.main, name ='main'),
    # url(r'^usermain$',bubbles_views.usermain, name ='usermain'), 
    # url(r'^register$',bubbles_views.register, name ='register'),
    # url(r'^addchat$', bubbles_views.addchat,name = 'addchat'),
    # url(r'^getlist$', bubbles_views.getlist,name='getlist'),
    # url(r'^logout$', auth_views.logout_then_login,name='logout'),
    # url(r'^gettime$', bubbles_views.gettime,name='gettime'),
    # url(r'^viewresult$', bubbles_views.viewresult,name='viewresult'),
    # url(r'^profile/(?P<id>\d+)$', bubbles_views.profile,name='profile'),
    # url(r'^add_Like/(?P<id>\d+)$', bubbles_views.addLikes,name='add_Like'),
    # url(r'^showresult$', bubbles_views.showresult,name='showresult'),
    # url(r'^share$', bubbles_views.share,name='share'),
    # url(r'^feedback$', bubbles_views.feedback,name='feedback'),
]