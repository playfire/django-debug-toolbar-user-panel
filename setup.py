#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-debug-toolbar-user-panel',
    description="Panel for the Django Debug toolbar to quickly switch between "
        "users.",
    version='0.1',
    url='http://code.playfire.com/',

    author='Playfire.com',
    author_email='tech@playfire.com',
    license='BSD',

    packages=find_packages(),
)
