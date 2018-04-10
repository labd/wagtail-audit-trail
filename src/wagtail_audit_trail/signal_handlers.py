import json

from wagtail.core.models import get_page_models
from wagtail.core.signals import page_published

from wagtail_audit_trail import models, diff
from wagtail_audit_trail.utils import current_user


def record_page_publish(instance, **kwargs):
    last_revision = (
        models.PageRecord.objects.get_latest_published_revision(instance))

    if last_revision:
        data_diff = diff.page_revision_diff(last_revision, instance)
    else:
        data_diff = ''

    user = current_user()
    models.PageRecord.objects.create(
        page=instance,
        page_url=instance.url,
        revision=instance.live_revision,
        diff=json.dumps(data_diff),
        user=user,
        user_fullname=user.get_full_name() if user else '',
    )


def register_signal_handlers():
    for model in get_page_models():
        page_published.connect(record_page_publish, sender=model)
