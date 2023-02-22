from django.urls import path
from .views import PaymentView, PaidView

urlpatterns = [
    path("", PaymentView.as_view(), name="shop"),
    path("paid", PaidView.as_view(), name="paid")
]
