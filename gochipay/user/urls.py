from django.urls import path
from gochipay.user.views import ReadView


urlpatterns = [
    path("read", ReadView.as_view(), name="read")
]
