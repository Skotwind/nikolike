from django.urls import re_path
from .views import test,Photos
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path('test1/', test.test1),
    re_path('main/', Photos.showall),
    re_path('test2/', test.test2),
    re_path('test3/', test.test3),
    re_path('my_profile/', test.acc),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)