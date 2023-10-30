"""
URL configuration for MedicalShop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from MedicalApp.views import index,about,contact,loginview,signup,View_Medicines_User
from MedicalApp import admin_urls,user_urls,pharmacy_urls

urlpatterns = [
    # path('admin/', admin.site.urls),/
    path('',index.as_view()),
    path('about',about.as_view()),
    path('contact',contact.as_view()),
    path('login',loginview.as_view()),
    path('admin/',admin_urls.urls()),
    path('signup',signup.as_view()),
    path('user/',user_urls.urls()),
    path('pharmacy/',pharmacy_urls.urls()),
    path('allmedicines',View_Medicines_User.as_view()),
    # path('medicine',single_medicine.as_view())

]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)