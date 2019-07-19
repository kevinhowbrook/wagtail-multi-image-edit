from django.conf import settings

from django.contrib.auth import get_user_model
from django.urls import reverse
from wagtail.images import get_image_model
from wagtail.images.tests.utils import (get_test_image_file,
                                        get_test_image_file_jpeg)
from wagtail.tests.utils import WagtailPageTests, WagtailTestUtils
from django.test import TestCase, override_settings


Image = get_image_model()


class MultiImageEditTests(TestCase, WagtailTestUtils):
    def setUp(self):
        super().setUp()
        self.login()
        image = Image.objects.create(title="Test image", file=get_test_image_file())
        self.image_id = image.id
        self.image_title = image.title

    def test_admin(self):
        response = self.client.get(reverse("wagtailadmin_home"))
        self.assertEqual(response.status_code, 200)

    def test_image_admin(self):
        response = self.client.get("/admin/images/")
        self.assertEqual(response.status_code, 200)

    def test_multi_image_edit_admin(self):
        response = self.client.get(reverse("multi_image_edit"))
        self.assertEqual(response.status_code, 200)

    def test_images_have_select_option(self):
        response = self.client.get("/admin/images/")
        self.assertContains(
            response,
            '<input type="checkbox" name="select_image" value="{}" class="toggle-select-row"/>'.format(
                self.image_id
            ),
        )

    # test the image is in the form
    def test_multi_edit_view(self):
        url = "{}?id={}".format(reverse("multi_image_edit"), self.image_id)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # test the form is there
    def test_multi_edit_view_form(self):
        url = "{}?id={}".format(reverse("multi_image_edit"), self.image_id)
        response = self.client.get(url)
        self.assertContains(
            response,
            '<form action="/admin/images/multi-edit/" method="POST" novalidate class="multi-image-edit-form">'.format(
                self.image_id
            ),
        )

    # test posting data to the form
    def test_image_update_post(self):
        # Submit
        url = "{}?id={}".format(reverse("multi_image_edit"), self.image_id)
        response = self.client.get(url)
        post_data = {
            "image-{}-title".format(self.image_id): "Dana Scully",
            "image_id": self.image_id,
        }
        response = self.client.post(reverse("multi_image_edit"), post_data)
        image = Image.objects.get(id=self.image_id)
        self.assertEqual("Dana Scully", image.title)
