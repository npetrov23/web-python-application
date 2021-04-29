from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('indicators/', include('indicators.urls')),
    path('', RedirectView.as_view(url='/indicators/')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

