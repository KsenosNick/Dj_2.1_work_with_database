from django.db import models


class Phone(models.Model):
    # id, name, price, image, release_date, lte_exists и slug
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    image = models.ImageField(upload_to='images/')
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=True)
    slug = models.SlugField(null=True, db_index=True, verbose_name="URL")


