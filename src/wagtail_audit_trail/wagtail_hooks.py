from django.urls import reverse
from django.conf.urls import url
from wagtail.core import hooks
from wagtail.admin.menu import MenuItem
from wagtail_audit_trail import views

@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        url(r'^audit-trail/pages/$',
            views.PageRecordListView.as_view(),
            name='audit_trail_pagerecord_list'),

        url(r'^audit-trail/pages/(?P<pk>\d+)$',
            views.PageRecordDetailView.as_view(),
            name='audit_trail_pagerecord_detail'),
    ]



@hooks.register('register_admin_menu_item')
def register_frank_menu_item():
  return MenuItem('Audit Trail',
    reverse('audit_trail_pagerecord_list'),
    classnames='icon icon-folder-inverse', order=10000)
