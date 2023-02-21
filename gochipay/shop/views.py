from django.shortcuts import render
from gochipay.shop.models import Payments, Shops
from django.views.generic import TemplateView


class PaymentView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        
        shop_id = self.request.GET.get("shop_id")
        price = self.request.GET.get("price")
        
        payment = Payments.objects.create(
            shop = Shops.objects.get(id=shop_id),
            price = price
        )

        payment.save()

        return context
