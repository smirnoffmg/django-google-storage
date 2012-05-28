=====================
django-google-storage
=====================

It' just a compilation of django-storages and boto to improve you
abilities to use Google Storage. It's easy and fast.

Install
=========

_Steps_


* pip install django-google-storage

* add 'django-google-storage' to your INSTALLED_APPS

* put 'django-google-storage.storage.GoogleStorage' in DEFAULT_FILE_STORAGE. 
It's in settings.py too.

* add GS_ACCESS_KEY_ID, GS_SECRET_ACCESS_KEY and GS_STORAGE_BUCKET_NAME 
to your settings.py

* ....

* PROFIT

# TODO
    - custom exceptions
    - testing