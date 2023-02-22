from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView


class TopView(TemplateView):
    template_name = "top.html"


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TopView.as_view(), name="top"),
    path("shop/", include("gochipay.shop.urls")),
    path("user/", include("gochipay.user.urls")),
]
