#!/usr/bin/env python
from pathlib import Path

from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="djangomako",
    version="1.3.2",
    packages=["djangomako"],
    install_requires=["Mako==1.2.3"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development",
    ],
    url="https://github.com/iamjazzar/django-mako",
    license="MIT License",
    author="Ahmed Jazzar",
    author_email="me@ahmedjazzar.com",
    description="The simple, elegant Django Mako library",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
