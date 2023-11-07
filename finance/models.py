from django.db import models
from django.contrib.auth import get_user_model
from products.models import Animation

class Payment(models.Model):
    TYPE_PAYMENT = (
        ("TO_COMPANY", "TO_COMPANY"),
        ("TO_USER", "TO_USER"),
    )
    user = models.ForeignKey(get_user_model(), related_name="my_animations", on_delete=models.PROTECT)
    type_pay = models.CharField(max_length=255, choices=TYPE_PAYMENT, default="TO_COMPANY")
    animation = models.ForeignKey(Animation, related_name="users_animations", on_delete=models.PROTECT)
    amount = models.IntegerField(default=0)
    date_paid = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.animation.owner:
            self.type_pay="TO_OWNER"
        return super().save(*args, **kwargs)
