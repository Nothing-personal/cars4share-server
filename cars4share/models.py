from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


# This code is triggered whenever a new user has been created and saved to the database
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)


class Document(models.Model):
    PASSPORT = 'P',
    DRIVER_LICENSE = 'D',
    CAR_DOCUMENTS = 'C',
    DOCUMENT_TYPES = (
        (DRIVER_LICENSE, 'Driver license'),
        (CAR_DOCUMENTS, 'Car documents'),
        (PASSPORT, 'Passport')
    )

    type = models.CharField(
        max_length=1,
        choices=DOCUMENT_TYPES,
    )


class CreditCard(models.Model):
    card_number = models.CharField(max_length=16)
    cardholder_name = models.CharField(max_length=30)
    cvv_code = models.CharField(max_length=3)
    due_date = models.DateField('due date')


class Feedback(models.Model):
    message = models.CharField(max_length=200, blank=True)
    rate = models.IntegerField()


class User(models.Model):

    MALE = 'M'
    FEMALE = 'F'
    SEX_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    LESSOR = 'LR'
    LESSEE = 'LE'
    ACCOUNT_TYPES = (
        (LESSOR, 'Lessor'),
        (LESSEE, 'Lessee'),
    )

    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=25)
    date_of_birth = models.DateField('date of birth')
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
        default=MALE,
    )
    is_verified = models.BooleanField(default=False)
    passport = models.OneToOneField('Document', related_name='passport', blank=True)
    driver_license = models.OneToOneField('Document', related_name='driver_license', blank=True)
    credit_card = models.ForeignKey(CreditCard, blank=True)  # need to think about should we store this data or not
    feedback = models.ManyToManyField(Feedback, blank=True)
    account_type = models.CharField(
        max_length=2,
        choices=ACCOUNT_TYPES,
    )
