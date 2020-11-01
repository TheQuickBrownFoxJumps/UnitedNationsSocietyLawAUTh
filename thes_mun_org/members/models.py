import datetime

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from django.utils.html import format_html

from simple_history.models import HistoricalRecords

# Create your models here.
"""
        *** Here is the model for the All Members. ***

Characteristics: 
Name
Surname
Sex
Birth day
Member e-mail
Phone
initialize entry date 
Educational background
Bio (not necessary, not public)
"""


class Member(models.Model):
    class EducationBackground(models.TextChoices):
        UNDERGRADUATE = 'UG', _('Undergraduate')
        POSTGRADUATE = 'PG', _('Postgraduate')
        GRADUATE = 'GR', _('Graduate')
        OTHER = 'OT', _('Other')

    class Sex(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')
        OTHER = 'O', _('Other')

    paid, not_paid, deadline, late = 'Paid', 'Not Paid', 'Deadline', 'Late'
    PAYMENT = (
        (paid, 'Paid'),
        (not_paid, 'Not Paid'),
        (deadline, 'Deadline'),
        (late, 'Late')
    )

    # Name
    name = models.CharField(max_length=128, default='No name given')
    # Surname
    surname = models.CharField(max_length=128, default='No surname given')
    # Birth day
    birth_date = models.DateTimeField('birth day')
    # Primary key
    id = models.AutoField(primary_key=True)
    # Member e-mail
    mail = models.EmailField(max_length=254)
    # Member sex-gender
    sex = models.CharField(
        max_length=2,
        choices=Sex.choices,
        default=Sex.OTHER,
    )
    # Member educational background
    education_background = models.CharField(
        max_length=2,
        choices=EducationBackground.choices,
        default=EducationBackground.OTHER,
    )
    # Payment
    payment = models.CharField(
        max_length=100,
        choices=PAYMENT,
        default=not_paid,
    )
    # Member phone
    phone = models.CharField(max_length=128, default='No phone given')
    # Sign up date for member
    init_date = models.DateTimeField('date created')
    # Last Payment Date
    last_payment_date = models.DateTimeField('date paid')
    # A brief biography and MUN experience
    mun_exp_bio = models.TextField(verbose_name='Experience', max_length=500, default='No bio given.')
    # Model DB History
    history = HistoricalRecords()

    # Finds and sets real payment value to payment based on last_payment_date
    def paid_not_paid(self):
        now = timezone.now()
        paid_time = datetime.timedelta(days=355)
        deadline = datetime.timedelta(days=385)
        not_paid = datetime.timedelta(days=730)
        if self.last_payment_date <= now < self.last_payment_date + paid_time:
            self.payment = 'Paid'
        elif self.last_payment_date + paid_time <= now < self.last_payment_date + deadline:
            self.payment = 'Deadline'
        elif self.last_payment_date + deadline <= now < self.last_payment_date + not_paid:
            self.payment = 'Not Paid'
        elif self.last_payment_date + not_paid <= now:
            self.payment = 'Late'
        return self.payment

    paid_not_paid.admin_order_field = 'payment'
    paid_not_paid.short_description = 'True payment'

    # Finds chosen value from admin payment field and paints background
    # (payment_status and paid_not_paid maybe different, client might want to mark an entry.)
    def payment_status(self):
        colors = {
            'Paid': 'green',
            'Not Paid': 'red',
            'Deadline': 'yellow',
            'Late': 'black',
        }

        if colors[self.payment] == 'black':
            return mark_safe(format_html(
                '<b style="color:white;background:{};">{}</b>',
                colors[self.payment],
                self.payment
            ))
        else:
            return mark_safe(format_html(
                '<b style="background:{};">{}</b>',
                colors[self.payment],
                self.payment
            ))

    payment_status.admin_order_field = 'payment'
    payment_status.short_description = 'Database Payment'

    def created_years_ago(self):
        now = timezone.now()
        return now - datetime.timedelta(days=365) >= self.init_date

    created_years_ago.admin_order_field = 'init_date'
    created_years_ago.boolean = True
    created_years_ago.short_description = 'More than one year?'


"""
        *** Here is the model for the Board Members. ***

Characteristics: 
Name
Surname
Sex
Member-profile-pic
Social Media account
Bio
"""


class BoardMember(models.Model):
    class Roles(models.TextChoices):
        PRESIDENT = 'P', _('President')
        VICE_PRESIDENT = 'VP', _('Vice-President')
        SECRETARY_GENERAL = 'SG', _('Secretary General')
        TREASURER = 'TR', _('Treasurer')
        ALTERNATE = 'AL', _('Alternate')

    class Sex(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')
        OTHER = 'O', _('Other')

    # Name
    name = models.CharField(max_length=128, default='No name given')
    # Surname
    surname = models.CharField(max_length=128, default='No surname given')
    # Board member sex-gender
    sex = models.CharField(
        max_length=2,
        choices=Sex.choices,
        default=Sex.OTHER,
    )
    # Member pic
    member_pic = models.ImageField(
        null=True,
        blank=True,
        upload_to='media/members/members_pic',
        default='media/members/members_pic/default_profile_pic.jpg', )
    # Board member role
    role = models.CharField(
        max_length=2,
        choices=Roles.choices,
        default=Roles.ALTERNATE, )
    # Social media link
    social_url = models.URLField(max_length=200, default='www')
    # Bio (available for public)
    member_bio = models.TextField(verbose_name='Experiences', max_length='500', default='(will be public)')
    # Model DB History
    history = HistoricalRecords()
