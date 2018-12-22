#!/usr/bin/env python
from setuptools import setup

setup(
    name='djangomako',
    version='1.2.1',
    packages=['djangomako'],
    install_requires=['Mako==1.0.7'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 1.11',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development',
    ],
    url='https://github.com/ahmedaljazzar/django-mako',
    license='MIT License',
    author='Ahmed Jazzar',
    author_email='me@ahmedjazzar.com',
    description='The simple, elegant Django Mako library',
)
