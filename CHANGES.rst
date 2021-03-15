Change log
==========

4.5 (2021-03-15)
----------------
- update configuration for version 5 of ``isort``

- add support for Python 3.9


4.4 (2020-06-18)
----------------
- Fix for Zope 4.4.3 ZMI by adding explicit acquisition of name ``ZopeVersion``
  (`#9 <https://github.com/zopefoundation/Products.ExternalMethod/issues/9>`_)

- Fix failing linter.


4.3 (2019-05-18)
----------------
- Add support for the bookmarkable URLs ZMI feature
  (`Zope#635 <https://github.com/zopefoundation/Zope/issues/635>`_)


4.2 (2019-04-06)
----------------
- Packaging cleanup

- Add support for Python 3.8

- Linting and code coverage configuration for ``tox``


4.1 (2018-11-06)
----------------
- Update to Bootstrap ZMI requiring `Zope >= 4.0b6`.

- Add support for Python 3.7.

- Drop support for Python 3.4.


4.0 (2017-10-18)
----------------
- Add support for Python 3.4, 3.5 and 3.6.

- Add compatibility with Zope 4.


3.0 (2016-07-18)
----------------
- Remove HelpSys support.

- Remove ZODB3 as direct dependency. Now we are able to use ZODB 4.0
  and it is a dependency of Zope2 anyways

2.13.1 (2014-11-02)
-------------------
- Handle both `func_code` / `__code__` and `func_defaults` / `__defaults__`.


2.13.0 (2010-07-10)
-------------------
- Released as separate package.
