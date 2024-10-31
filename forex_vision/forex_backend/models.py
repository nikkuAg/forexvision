from django.db import models
from forex_backend.constants import CURRENCIES_QUOTE_CHOICES


class ExchangeRate(models.Model):
    date = models.DateField()
    quote = models.CharField(choices=CURRENCIES_QUOTE_CHOICES, max_length=10)
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()

    class Meta:
        ordering = ["quote", "date"]
        unique_together = ("date", "quote")

    def __str__(self):
        return f"{self.date} - {self.quote} - {self.close}"
