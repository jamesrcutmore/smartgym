from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.utils import timezone

rate_choices = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    rating = models.IntegerField(rate_choices)
    review_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment
