from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from wagtail.admin.utils import permission_denied
from wagtail.images import get_image_model
from wagtail.images.permissions import permission_policy

from .forms import MultiImageEditForm

Image = get_image_model()


def multi_image_edit(request):
    images = Image.objects.filter(id__in=request.GET.getlist("id"))
    if request.method == "GET":
        forms = []
        for image in images:
            instance = get_object_or_404(Image, id=image.id)
            if not permission_policy.user_has_permission_for_instance(
                request.user, "change", instance
            ):
                return permission_denied(request)

            form = MultiImageEditForm(
                request.POST or None, instance=instance, prefix="image-%d" % instance.id
            )
            forms.append(form)
        return render(request, "wagtail_multi_image_edit/multi_edit.html", {"forms": forms})
    elif request.method == "POST":
        image_id = request.POST["image_id"]
        instance = Image.objects.get(id=image_id)

        if not permission_policy.user_has_permission_for_instance(
            request.user, "change", instance
        ):
            return permission_denied(request)

        form = MultiImageEditForm(
            request.POST, instance=instance, prefix="image-%d" % instance.id
        )

        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            return JsonResponse(
                {
                    "success": False,
                    "form": render_to_string(
                        "wagtail_multi_image_edit/_multi_edit_form.html",
                        {"image": instance, "form": form},
                        request=request,
                    ),
                }
            )
