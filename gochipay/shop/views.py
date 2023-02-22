from gochipay.shop.models import Payments, Shops, Reviewes
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.urls import reverse


class PaymentView(TemplateView):
    template_name = "shop.html"

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        
        shop_id = self.request.GET.get("shop_id")
        price = self.request.GET.get("price")
        
        payment = Payments.objects.create(
            shop = Shops.objects.get(id=shop_id),
            price = price
        )

        payment.save()

        context["payment_id"] = payment.id

        return context


class PaidView(TemplateView):
    template_name = "paid.html"

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)

        payment_id = self.request.GET.get("payment_id")

        payment = Payments.objects.get(id=payment_id)
        context["shop"] = payment.shop
        context["price"] = payment.price

        return context


class WriteView(TemplateView):
    template_name = "write.html"

    def post(self, request):
        title = request.POST.get("title")
        message = request.POST.get("message")

        review = Reviewes.objects.create(
            title = title,
            message = message
        )

        review.save()

        return redirect(reverse("top"))


class ReviewView(TemplateView):
    template_name = "review.html"

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)

        shops = Shops.objects.all()

        context["shop"] = shops.first()
        context["reviews"] = Reviewes.objects.all()

        return context
