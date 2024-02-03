"""
URL configuration for wise_education project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static

from wise_education import settings

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.index,name="index"),
    path("our_alumni",views.our_alumni,name="our_alumni"),
    path("about_us",views.about_us,name="about_us"),
    path("ceo_message",views.ceo_message,name="ceo_message"),
    path("our_team",views.our_team,name="our_team"),
    path("executive_board",views.executive_board,name="executive_board"),
    path("ongoing_projects",views.ongoing_projects,name="ongoing_projects"),
    path("goverment_collaboration",views.goverment_collaboration,name="goverment_collaboration"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
