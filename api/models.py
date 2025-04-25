from django.db import models
from django.db.models import TextChoices


class VisitType(TextChoices):
    ONLINE = 'online', 'Online'
    OFFLINE = 'offline', 'Offline'


class Contact(models.Model):
    name = models.CharField("Имя", max_length=100)
    phone = models.CharField("Телефон", max_length=20)
    visit_form = models.CharField(max_length=50, choices=VisitType.choices, default=VisitType.ONLINE, verbose_name="Формат посещения")
    is_toastmasters  = models.BooleanField(default=False)
    club = models.CharField(max_length=200, null=True, blank=True, verbose_name="Название клуба")

    created_at = models.DateTimeField("дата создания", auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.phone})"

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Telephone(models.Model):
    name = models.CharField("Имя", max_length=100)
    phone = models.CharField("Телефон", max_length=20)

    def __str__(self):
        return f"{self.name} ({self.phone})"

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'
