"""ShoreCapital URL Configuration

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
from django.conf.urls.static import static
from django.urls import path, re_path
import Contact.views
import Pages.views
from ShoreCapital import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^referral/.*$', Pages.views.ReferralView.as_view(), name="referral"),
    path('career/', Pages.views.CareerView.as_view(), name="career"),
    path('sell/', Pages.views.SellView.as_view(), name="sell"),
    path('buy/', Pages.views.BuyView.as_view(), name="buy"),
    path('', Pages.views.HomeView.as_view(), name="home"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
