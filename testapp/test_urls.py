from django.urls import re_path
from .views import test

urlpatterns = [
    re_path('test1/', test.test1),
    re_path('main/', test.main),
    re_path('test2/', test.test2),
    re_path('test3/', test.test3),
    re_path('my_profile/', test.acc),

]