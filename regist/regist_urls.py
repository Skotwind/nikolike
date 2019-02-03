from django.urls import re_path
from .views import regist

urlpatterns = [
    re_path('regist/', regist.reg),
    re_path('login/', regist.login),
    re_path('logout/', regist.logout),
    re_path('account/', regist.show),
    re_path('newname/', regist.newname),
]