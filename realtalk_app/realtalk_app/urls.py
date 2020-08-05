from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path

from pages import views # import Views from any app to see them

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage_view, name='home'),# One way to write out URLS
    path('about/', views.about_view, name='about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
