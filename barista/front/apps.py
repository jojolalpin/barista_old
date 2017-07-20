from __future__ import unicode_literals

from django.apps import AppConfig


class FrontConfig(AppConfig):
    name = 'barista.front'
    verbose_name = "Front"

    def ready(self):
        """Override this to put in:
            Front system checks
            Front signal registration
        """
        pass

