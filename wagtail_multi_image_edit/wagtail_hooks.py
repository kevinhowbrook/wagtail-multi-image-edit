from django.templatetags.static import static
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from wagtail.core import hooks


@hooks.register("insert_global_admin_js")
def global_admin_js():
    return mark_safe(
        '<script src="%s"></script>'
        % static("wagtail_multi_image_edit/admin/js/wagtail_multi_image_edit.js")
    )


@hooks.register("insert_global_admin_css")
def global_admin_css():
    return format_html(
        '<link rel="stylesheet" href="%s">'
        % static("wagtail_multi_image_edit/admin/css/wagtail_multi_image_edit.css")
    )
