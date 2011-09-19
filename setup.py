#!/usr/bin/env python

from distutils.core import setup

setup(
    name='django-debug-toolbar-user-panel',
    description="Panel for the Django Debug toolbar to quickly switch between "
        "users.",
    version='0.1',
    url='http://code.playfire.com/',

    author='Playfire.com',
    author_email='tech@playfire.com',
    license='BSD',

    packages=(
        'debug_toolbar_user_panel',
    ),
    package_data={'': [
        'templates/debug_toolbar_user_panel/*',
    ]},
)
