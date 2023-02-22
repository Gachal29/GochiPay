import uuid
import datetime
from django.db import models


class Shops(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, verbose_name="店名")
    image = models.ImageField(upload_to="ShopImages/")

    class Meta:
        verbose_name = "登録店"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.id}: {self.name}"


class Payments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shop = models.ForeignKey(Shops, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name="支払い金額")
    is_paid = models.BooleanField(default=False, verbose_name="支払い状況")
    date = models.DateTimeField(default=datetime.datetime.now(), verbose_name="決済日時")

    class Meta:
        verbose_name = "決済記録"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.id}: {self.shop} <{self.date}>"
