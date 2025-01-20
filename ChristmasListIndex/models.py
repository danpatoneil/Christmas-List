# import the standard Django Model
# from built-in library
from django.db import models
from datetime import datetime

class GiftIdea(models.Model):

    # Field Names
    title = models.CharField(max_length=200)
    description = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/%Y/%m/%d")
    link = models.URLField()
    purchased = models.BooleanField(default=False)
    suggested_amount = models.DecimalField(max_digits=6, decimal_places=2)

    # rename the instances of the model
    # with their title name
    def __str__(self) -> str:
        return self.title

