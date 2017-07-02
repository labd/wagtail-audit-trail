from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.blocks import ImageChooserBlock


class ContentPage(Page):
    body = StreamField([
        ('image', ImageChooserBlock()),
    ], default="")

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
