from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

# Create your models here.
from commons.models import DocumentType, Gender
from .managers import UserManager


class AbstractETruck(models.Model):
    is_active = models.BooleanField(
        default=True,
        verbose_name=("Is active")
    )
    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name=("Created At")
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=("Updated At")
    )
    updated_by = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="+",
        verbose_name=("Updated By")
    )
    created_by = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="+",
        verbose_name=("Updated By")
    )

    class Meta:
        verbose_name = "ETrack Abstract Class"
        abstract = True

    def save(self, *args, **kwargs):
        user = 'accounts.User'
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.updated_by = user

        super(AbstractETruck, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()


class User(AbstractUser):
    username = models.CharField(max_length=255, blank=True, )
    first_name = models.CharField(_('first name'), max_length=150)
    last_name = models.CharField(_('last name'), max_length=150)

    email = models.EmailField(
        verbose_name='email address',
        help_text=_('Correo electrónico'),
        max_length=255,
        unique=True,
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email


class Profile(AbstractETruck):
    """
        Profile model
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
    )

    gender = models.ForeignKey(
        Gender,
        on_delete=models.CASCADE,
    )
    document_type = models.ForeignKey(
        DocumentType,
        on_delete=models.CASCADE,
    )
    document = models.CharField(
        max_length=15,
        unique=True
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )
    avatar = models.ImageField(
        upload_to="core/static/images/avatar/",
        default='core/static/images/avatar/default.jpeg',
    )
    phone = models.CharField(
        max_length=20,
        blank=True
    )
    is_phone_verified = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return self.user.email

    def _gender(self):
        return self.gender.long_name

    def _document_type(self):
        return self.document_type.short_name
