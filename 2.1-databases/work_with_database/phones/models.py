from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50, null=False)
    price = models.IntegerField(default=0)
    image = models.URLField(max_length=300)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=50)