from gochipay.shop.models import Payments, Shops
from django.views.generic import TemplateView


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


class ReviewView(TemplateView):
    template_name = "review.html"
