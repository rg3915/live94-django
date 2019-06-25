from django.db import models
from django.contrib.auth.models import User


class Live(models.Model):
    title = models.TextField('título')
    guest = models.ForeignKey(
        User,
        verbose_name='convidado',
        related_name='guests',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title

    def to_dict_json(self):
        data = {
            'pk': self.pk,
            'title': self.title,
        }
        return data
