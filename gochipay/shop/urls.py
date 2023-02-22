from django.urls import path
from .views import PaymentView, PaidView, WriteView, ReviewView

urlpatterns = [
    path("", PaymentView.as_view(), name="shop"),
    path("paid", PaidView.as_view(), name="paid"),
    path("write", WriteView.as_view(), name="write"),
    path("review", ReviewView.as_view(), name="review")
]
