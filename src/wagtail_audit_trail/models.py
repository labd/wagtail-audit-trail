import json

from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.functional import cached_property

User = get_user_model()


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        User,
        related_name='+',
        on_delete=models.SET_NULL,
        null=True,
        blank=True)

    user_fullname = models.CharField(max_length=500, blank=True)

    class Meta:
        abstract = True


class PageRecordManager(models.Manager):
    def get_latest_published_revision(self, page):
        """Return the latest published revision for the page"""
        record = (
            self.filter(page=page)
            .select_related('revision')
            .order_by('-created_at')
            .first())
        if record:
            return record.revision.as_page_object()


class PageRecord(Record):
    page = models.ForeignKey(
        'wagtailcore.Page',
        related_name='+',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    page_url = models.CharField(max_length=1024, null=True, blank=True)

    revision = models.ForeignKey(
        'wagtailcore.PageRevision',
        related_name='+',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    diff = models.TextField(blank=True)

    objects = PageRecordManager()

    class Meta:
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('audit_trail_pagerecord_detail', kwargs={'pk': self.pk})

    @cached_property
    def diff_json(self):
        return json.loads(self.diff)

    @cached_property
    def previous_record(self):
        return (
            self.__class__.objects
            .filter(page_id=self.page_id, created_at__lt=self.created_at)
            .order_by('-created_at')
            .first())

    @cached_property
    def previous_revision(self):
        record = self.previous_record
        if record and record.revision_id:
            return record.revision

    @cached_property
    def compare_url(self):
        if self.previous_revision:
            return reverse('wagtailadmin_pages:revisions_compare', args=[
                self.page_id,
                self.previous_revision.pk,
                self.revision_id])

