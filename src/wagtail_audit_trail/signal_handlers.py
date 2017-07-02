import json

from wagtail.wagtailcore.models import get_page_models
from wagtail.wagtailcore.signals import page_published

from wagtail_audit_trail import models, diff


def record_page_publish(instance, **kwargs):
    last_revision = (
        models.PageRecord.objects.get_latest_published_revision(instance))

    if last_revision:
        data_diff = diff.page_revision_diff(last_revision, instance)

    # Create the audit trail object. Since wagtail does not (yet) send the
    # user in the signal who published the revision we leave it empty for now
    models.PageRecord.objects.create(
        page=instance,
        revision=instance.live_revision,
        diff=json.dumps(data_diff),
        user=None)


def register_signal_handlers():
    for model in get_page_models():
        page_published.connect(record_page_publish, sender=model)
