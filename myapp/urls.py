from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('crud/',include('crud.urls')),
    path('relationapp/',include('relationapp.urls')),
    path('databaseapp/',include('databaseapp.urls')),
    path("restapp/",include('restapp.urls')),
    path('sessioncookies/',include('sessioncookies.urls')),
    path('signalapp/',include('signalapp.urls')),
    path('authapp/',include('authapp.urls')),
    # path('accounts/',include('customUserAuth.urls')),
    # path('authtokkenapp/',include('authtokkenapp.urls')),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 