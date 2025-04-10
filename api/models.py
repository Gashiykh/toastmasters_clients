from django.db import models

class Contact(models.Model):
    name = models.CharField("Имя", max_length=100)
    phone = models.CharField("Телефон", max_length=20)
    created_at = models.DateTimeField("дата создания", auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.phone})"

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
