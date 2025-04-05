import uuid

from django.db import models
from django.db.models import Model, UniqueConstraint


class Address(Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    street = models.TextField()
    city = models.TextField()
    postcode = models.TextField()
    council = models.TextField()

    class Meta:
        db_table = 'app_version'
        constraints = [
            UniqueConstraint(fields=["street", "city", "postcode"],
                             name="unique_street_city_postcode")
        ]


class RubbishType(Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()


class CollectionSchedule(Model):
    class CollectionFrequency(models.TextChoices):
        WEEKLY = 'W', 'Weekly'
        BIWEEKLY = 'B', 'Bi-Weekly'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    rubbish_type = models.ForeignKey(RubbishType, on_delete=models.RESTRICT)
    frequency = models.CharField(
        max_length=1,
        choices=CollectionFrequency.choices,
    )
    start_date = models.DateField()
    import_date = models.DateField()
