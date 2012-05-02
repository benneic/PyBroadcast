#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pybroadcast',
    version='0.0.1',
    description='Roamz Broadcast API Client',
    author='Roamz',
    author_email='support@roamz.com',
    url='http://www.roamz.com/',
    packages=['pybroadcast'],
    install_requires=[
        'bunch==1.0.1',
        'requests>=0.9.1,<1.0',
        'simplejson==2.3.2',
    ]
)
