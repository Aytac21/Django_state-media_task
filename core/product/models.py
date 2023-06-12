from django.db import models
from ckeditor.fields import RichTextField

class Product(models.Model):
    name = models.CharField(max_length=300)
    description = RichTextField(blank=True, null=True)
    price = models.FloatField()

    def __str__(self):
        return self.name


def upload_to(instance, filename):
    return f"products/{instance.product.name.lower()}/{filename}"

def upload_to_company(instance, filename):
    return f"companies/{instance.product.name.upper()}/{filename}"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_to)
    company_logo = models.ImageField(upload_to=upload_to_company)

    def __str__(self):
        return self.product.name