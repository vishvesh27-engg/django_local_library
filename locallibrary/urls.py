"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
from django.urls import include

urlpatterns += [
    path('catalog/', include('catalog.urls')),
]
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
urlpatterns += [
    path('accounts/ login', include('django.contrib.auth.urls'),name='login'),
]
urlpatterns += [
    path('accounts/ logout', include('django.contrib.auth.urls'),name='logout'),
]
urlpatterns += [
    path('accounts/ password_change', include('django.contrib.auth.urls'),name='password_change'),
]
urlpatterns += [
    path('accounts/ password_change/done', include('django.contrib.auth.urls'),name='password_change_done'),
]
urlpatterns += [
    path('accounts/ password_reset', include('django.contrib.auth.urls'),name='password_reset'),
]
urlpatterns += [
    path('accounts/ password_reset/done', include('django.contrib.auth.urls'),name='password_reset_done'),
]
urlpatterns += [
    path('accounts/ reset/<uidb64>/<token>', include('django.contrib.auth.urls'),name='password_reset_confirm'),
]
urlpatterns += [
    path('accounts/ reset/done', include('django.contrib.auth.urls'),name='password_reset_complete'),
]

