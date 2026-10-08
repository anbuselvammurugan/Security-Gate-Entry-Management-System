from django.db import models


class Visitor(models.Model):

    STATUS_CHOICES = [
        ('IN', 'Inside'),
        ('OUT', 'Checked Out'),
    ]

    visitor_name = models.CharField(max_length=100)

    phone = models.CharField(max_length=15)

    company = models.CharField(
        max_length=150,
        blank=True
    )

    purpose = models.CharField(max_length=255)

    person_to_meet = models.CharField(max_length=100)

    vehicle_number = models.CharField(
        max_length=20,
        blank=True
    )

    check_in = models.DateTimeField(
        auto_now_add=True
    )

    check_out = models.DateTimeField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='IN'
    )

    def __str__(self):
        return self.visitor_name
