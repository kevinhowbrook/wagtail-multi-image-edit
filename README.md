[![CircleCI](https://circleci.com/gh/kevinhowbrook/wagtail-multi-image-edit.svg?style=shield&circle)](https://circleci.com/gh/kevinhowbrook/wagtail-multi-image-edit)

# Wagtail Multi Image Edit

_Wagtail Multi Image Edit offers a solution to editing and updating data fields for multiple images from one place._


<p align="center">

![multi image edit eg](https://i.imgur.com/ijVJ4sf.png)

![multi image edit form](https://i.imgur.com/4RVtZXi.png)

</p>

## Installation

Wagtail Multi Image Edit has a pypi package and can be installed with:

```
pip install wagtail-multi-image-edit
```

After installing, add it to `INSTALLED_APPS` in your settings file

```python
INSTALLED_APPS = [
    ...
    'wagtail_multi_image_edit',
]
```

Add the new url pattern and view import to `urls.py`:

```python
from wagtail_multi_image_edit.views import multi_image_edit

urlpatterns = [
    url(r'^admin/images/multi-edit/', multi_image_edit, name='multi_image_edit'),
```

Add the needed templates by adding the following to your settings where TEMPLATES is defined:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [
            'wagtail_multi_image_edit/templates'
            ],
        ...
```

Finally, add which fields you want to be exposed by adding the following to your settings:

```python
MULTI_IMAGE_EDIT_FIELDS = [
    'title',
    'collection',
    'tags',
]
```

### Note
The plugin will override the core wagtail template `wagtailimage/images/results` so select boxes can be added. You may need to carry out extra template work if you are already customising this core template.

## Thank you to...

[@katestatton](https://twitter.com/katestatton) For the initial concept and direction.

[@gasman](https://github.com/gasman) For code guidance and form validation.

[@noslouch](https://github.com/noslouch) For great JS feedback.
