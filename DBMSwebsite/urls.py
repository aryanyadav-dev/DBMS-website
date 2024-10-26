from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('admin-confs',admin.site.urls),
    path('',include('files.urls'))
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
