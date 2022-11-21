from django.urls import path, include
from .views import *

from django.conf import settings
from django.conf.urls.static import static


app_name = "core"

urlpatterns = [
    path('', home, name='home'),
    path('upload', createpost, name='upload'),
    
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)