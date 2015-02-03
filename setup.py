# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='django-google-storage',
    version='0.4.0',
    packages=['django-google-storage', ],
    author='Maxim Smirnoff',
    author_email='smirnoffmg@gmail.com',
    url='http://pypi.python.org/pypi/django-google-storage/',
    license='LICENSE.txt',
    description='Django storage for Google Storage',
    install_requires=[
        "Django >= 1.4",
        "boto",
    ],
)
