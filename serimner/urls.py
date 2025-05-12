"""
URL configuration for serimner project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from baton.autodiscover import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings
from django.conf.urls.static import static

from home.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path('baton/', include('baton.urls')),
    path("", include("home.urls")),
    path("gallery/", include("gallery.urls")),
    # Direct favicon.ico requests to the correct static file
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/favicon/favicon.ico'))),
    # Direct site.webmanifest requests explicitly
    path('site.webmanifest', RedirectView.as_view(url=staticfiles_storage.url('images/favicon/site.webmanifest'))),
]

# Add this for development environment
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
