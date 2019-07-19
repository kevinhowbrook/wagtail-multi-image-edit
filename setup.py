#!/usr/bin/env python
"""
Installs yourapp.
"""

from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="Wagtail Multi Image Edit",
    version="0.0.5",
    description="Wagtail Multi Image Edit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kevinhowbrook/wagtail-multi-image-edit",
    author="Kevin Howbrook",
    author_email="kbhowbrook@gmail.com",
    license="MIT License",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    install_requires=["wagtail"],
)
