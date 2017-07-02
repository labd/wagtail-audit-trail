from django.apps import AppConfig, apps
from django.conf import settings


class WagtailAuditTrailConfig(AppConfig):
    name = 'wagtail_audit_trail'
    label = 'wagtail_audit_trail'
    verbose_name = "Wagtail Audit Trail"

    def ready(self):
        from wagtail_audit_trail.signal_handlers import register_signal_handlers

        register_signal_handlers()
