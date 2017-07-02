from django.views import generic

from wagtail_audit_trail import models


class PageRecordListView(generic.ListView):
    queryset = models.PageRecord.objects.all()


class PageRecordDetailView(generic.DetailView):
    queryset = models.PageRecord.objects.all()
