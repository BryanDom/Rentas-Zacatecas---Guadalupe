from django.contrib import admin
from Propiedades.views import Bienvenida
from perfiles.views import CustomLoginView
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Propiedades/', include('Propiedades.urls')),
    path('', CustomLoginView.as_view(), name="login"),
    path('home/', Bienvenida.as_view(), name="bienvenida"),
    path('perfiles/', include('perfiles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
