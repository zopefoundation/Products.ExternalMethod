##############################################################################
#
# Copyright (c) 2010 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

from setuptools import find_packages
from setuptools import setup


setup(name='Products.ExternalMethod',
      version='6.1.dev0',
      url='https://github.com/zopefoundation/Products.ExternalMethod',
      project_urls={
          'Issue Tracker': ('https://github.com/zopefoundation/'
                            '/Products.ExternalMethod/issues'),
          'Sources': ('https://github.com/zopefoundation/'
                      'Products.ExternalMethod'),
      },
      license='ZPL-2.1',
      description='This package provides support for external Python methods '
      'within a Zope environment.',
      author='Zope Foundation and Contributors',
      author_email='zope-dev@zope.dev',
      long_description=(open('README.rst').read() + '\n' +
                        open('CHANGES.rst').read()),
      long_description_content_type='text/x-rst',
      packages=find_packages('src'),
      namespace_packages=['Products'],
      package_dir={'': 'src'},
      classifiers=[
          'Development Status :: 6 - Mature',
          'Environment :: Web Environment',
          'Framework :: Zope',
          'Framework :: Zope :: 5',
          'License :: OSI Approved :: Zope Public License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
          'Programming Language :: Python :: 3.12',
          'Programming Language :: Python :: 3.13',
          'Programming Language :: Python :: Implementation :: CPython',
      ],
      python_requires='>=3.9',
      install_requires=[
          'setuptools',
          'AccessControl',
          'Acquisition',
          'ExtensionClass>=4.1a1',
          'Persistence',
          'ZODB',
          'Zope >= 4.0b6',
      ],
      include_package_data=True,
      zip_safe=False,
      )
