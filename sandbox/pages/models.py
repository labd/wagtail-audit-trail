from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock


class ContentPage(Page):
    body = StreamField([
        ('image', ImageChooserBlock()),
    ], default="")

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
