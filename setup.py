from setuptools import setup, find_packages
from os.path import dirname
import esteroids

setup(
    name    = '%s' % esteroid.__pkg_name__,
    version = esteroids.__version__,
    author  = esteroids.__author__,
    author_email = "alem@cidola.com",
    description  = esteroids.__desc__,
    license      = esteroids.__licence__,
    keywords     = "django, templates. bootstrap, bootstrap templates, crud templates, django-tables2, django-filter, django-crispy-forms",
    url          = "http://packages.python.org/%s" % esteroids.__pkg_name__,
    packages     = find_packages(),
    include_package_data = True,
    long_description = open('README.rst').read(),
    classifiers  = [
         'Environment :: Web Environment',
         'Framework :: Django',
         'Intended Audience :: Developers',
         "License :: OSI Approved :: %s" % esteroids.__licence__,
         'Operating System :: OS Independent',
         'Programming Language :: Python',
         'Programming Language :: Python :: 2.7',
         'Topic :: Internet :: WWW/HTTP',
         'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
