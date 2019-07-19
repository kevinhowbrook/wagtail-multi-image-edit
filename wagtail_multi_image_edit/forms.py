from django.conf import settings
from wagtail.images import get_image_model
from wagtail.images.forms import get_image_form

Image = get_image_model()

ImageForm = get_image_form(Image)


class MultiImageEditForm(ImageForm):
    class Meta(ImageForm.Meta):
        fields = settings.MULTI_IMAGE_EDIT_FIELDS
