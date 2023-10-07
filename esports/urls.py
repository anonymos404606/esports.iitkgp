
from django.contrib import admin
from django.urls import path, include
#added  to change admin name,title,etc.
admin.site.site_header = "E-Sports IITKGP"
admin.site.site_title = "E-Sports IITKGP"
admin.site.index_title = "E-Sports IITKGP"
#for media and static files purpose
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('sports.urls')),  
]
urlpatterns+=staticfiles_urlpatterns()

#during development only
if settings.DEBUG:
    urlpatterns=urlpatterns+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns=urlpatterns+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
