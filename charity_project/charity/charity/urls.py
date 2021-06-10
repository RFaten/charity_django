"""charity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from cases_app import views
from donations_app import views as donViews

urlpatterns = [
    path('', views.cases, name='cases'),
    path('admin/', admin.site.urls),
    path('cases_app/', include('cases_app.urls')),
    path('donors_app/', include('donors_app.urls')),
    path('donations_app/', include('donations_app.urls')),
    # path('<id>/', views.update_case, name='update_case'),
    path('donations_app/<id>/', donViews.update_donation, name='update_donation'),

    # RESTFUL URLS
    path('api/cases_app/', include('cases_app.api.urls')),
    path('api/donors_app/', include('donors_app.api.urls')),
    path('api/donations_app/', include('donations_app.api.urls')),
]
