from django.db import models
from django.utils.translation import ugettext as _

from pytracking import Configuration as _Configuration
from solo.models import SingletonModel


class Configuration(SingletonModel):
    webhook_url = models.CharField(
        max_length=512, blank=True, null=True, default='',
        verbose_name=_('URL Вебхука')
    )

    def get_configuration(self):
        return _Configuration(
            webhook_url=self.webhook_url,
        )

    def __str__(self):
        return 'Конфигурация'

    class Meta:
        ordering = ('id',)
        verbose_name = _('Конфигурация')
        verbose_name_plural = _('Конфигурация')
