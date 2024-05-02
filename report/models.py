from django.db import models

from realtors.models import Realtor
from listings.models import Listing
from contacts.models import Contact

# from accounts.models import U


class Report(models.Model):

    name: str = models.CharField(max_length=200)
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    listings = models.ForeignKey(Listing, on_delete=models.DO_NOTHING)
    contact = models.ForeignKey(Contact, on_delete=models.DO_NOTHING)


def __str__(self):
    return self.name
