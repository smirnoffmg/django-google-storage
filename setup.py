from distutils.core import setup

setup(
    name='django-google-storage',
    version='0.2dev',
    packages=['django-google-storage', ],
    author='Maxim Smirnoff',
    author_email='max@whitescape.com',
    url='http://pypi.python.org/pypi/django-google-storage/',
    license='LICENSE.txt',
    description='Django storage for Google Storage',
    long_description=open('README.txt').read(),
    install_requires=[
        "Django >= 1.4",
        "boto",
    ],
)
