from setuptools import setup, find_packages
from os.path import dirname
import steroids

setup(
    name    = '%s' % esteroid.__pkg_name__,
    version = steroids.__version__,
    author  = steroids.__author__,
    author_email = "alem@cidola.com",
    description  = steroids.__desc__,
    license      = steroids.__licence__,
    keywords     = "django, templates. bootstrap, bootstrap templates, crud templates, django-tables2, django-filter, django-crispy-forms",
    url          = "http://packages.python.org/%s" % steroids.__pkg_name__,
    packages     = find_packages(),
    include_package_data = True,
    install_requires=[
            "django-tables2",
            "django-crispy-forms",
            "django-filter",
        ],
    long_description = open('README.rst').read(),
    classifiers  = [
         'Environment :: Web Environment',
         'Framework :: Django',
         'Intended Audience :: Developers',
         "License :: OSI Approved :: %s" % steroids.__licence__,
         'Operating System :: OS Independent',
         'Programming Language :: Python',
         'Programming Language :: Python :: 2.7',
         'Topic :: Internet :: WWW/HTTP',
         'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
