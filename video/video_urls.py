from django.urls import re_path
from . import views

urlpatterns = [
    re_path('hello/', views.hello),
    re_path('all/', views.showall),
    re_path('get/(?P<video_id>\d+)/$', views.showone),
    re_path('addcomment/(?P<video_id>\d+)/$', views.addcomm),
    re_path('addlike/', views.addlike),
    re_path('addlikecom/', views.addlikecom),
]