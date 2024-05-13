from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.risk_calc, name='risk_calc'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)