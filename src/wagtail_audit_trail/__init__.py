import pkg_resources

__version__ = pkg_resources.get_distribution("wagtail_audit_trail").version

default_app_config = 'wagtail_audit_trail.apps.WagtailAuditTrailConfig'
