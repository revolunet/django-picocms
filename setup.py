#!/usr/bin/env python
from distutils.core import setup

# Dynamically calculate the version based on picocms.VERSION
version_tuple = __import__('picocms').VERSION
version = ".".join([str(v) for v in version_tuple])

setup(
    name = 'django-picocms',
    description = '''Simplest django CMS ever.''',
    version = version,
    author = 'Julien Bouquillon',
    author_email = 'julien@revolunet.com',
    url = 'http://github.com/revolunet/django-picocms',
    packages=['picocms'],
    install_requires=[
        'Django>=1.3.1,<1.5',
        'south>=0.7.2',
        'django-mptt>=0.5.1,<0.6'
    ],
    include_package_data = True,
    classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
)
