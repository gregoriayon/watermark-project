from django.db import models

# Create your models here.

class SalesModel(models.Model):
    product = models.CharField(max_length=120, null=True)
    price = models.PositiveIntegerField(null=True, default=0)
    quantity = models.PositiveIntegerField(default=0, null=True)

    def __str__(self):
        return f"Product Name: {self.id}-{self.product}, Quantity: {self.quantity}"
    
    class Meta:
        verbose_name = "Sale"
        verbose_name_plural = "Sales"
        ordering = ["-id"]
