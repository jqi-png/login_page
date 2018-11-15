from django.db import models

CHOICES = (
    ('TE', 'test engineer'),
    ('OP', 'operator'),
    )

class UserProfile(models.Model):
    email = models.CharField(max_length=100, default='none')
    barcode = models.IntegerField(default=0)
    role = models.CharField(max_length=100, default='none', choices=CHOICES)
