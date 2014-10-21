python\_dotted\_name\_resolver
==============================

|Build Status|  |PyPI Version|

`DottedNameResolver <http://docs.pylonsproject.org/projects/pyramid/en/latest/api/path.html#pyramid.path.DottedNameResolver>`__
and other stuff lifted from
`pyramid.path <http://docs.pylonsproject.org/projects/pyramid/en/latest/api/path.html>`__
from the wonderful
`Pyramid <http://docs.pylonsproject.org/projects/pyramid/>`__ web
framework.

A few quick examples of usage
-----------------------------

.. code:: python

    In [1]: from dotted_name_resolver import DottedNameResolver

    In [2]: r = DottedNameResolver()

    In [3]: r.resolve('os.path')
    Out[3]: <module 'posixpath' from
    '/Users/marca/python/virtualenvs/dotted_name_resolver/lib/python2.7/posixpath.pyc'>

    In [4]: r.resolve('os.path.exists')
    Out[4]: <function genericpath.exists>

    In [5]: r.resolve('dotted_name_resolver.DottedNameResolver.maybe_resolve')
    Out[5]: <unbound method DottedNameResolver.maybe_resolve>

    In [6]: import os.path

    In [7]: r.resolve(os.path.exists)
    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call
    last)
    <ipython-input-9-0fd311498cae> in <module>()
    ----> 1 r.resolve(os.path.exists)

    /Users/marca/dev/git-repos/python_dotted_name_resolver/dotted_name_resolver/__init__.pyc
    in resolve(self, dotted)
        328         if not isinstance(dotted, string_types):
    --> 329             raise ValueError('%r is not a string' % (dotted,))
        330         package = self.package
        331         if package is CALLER_PACKAGE:

    ValueError: <function exists at 0x1002a5398> is not a string

    In [8]: r.maybe_resolve(os.path.exists)
    Out[8]: <function genericpath.exists>

    In [24]: from dotted_name_resolver import AssetResolver

    In [25]: a = AssetResolver('IPython')

    In [26]: a.resolve('html/static/notebook/js/notebook.js').abspath()
    Out[26]:
    '/Users/marca/python/virtualenvs/dotted_name_resolver/lib/python2.7/site-packages/IPython/html/static/notebook/js/notebook.js'

Documentation
-------------

For detailed documentation, see `the documentation for pyramid.path
<http://docs.pylonsproject.org/projects/pyramid/en/latest/api/path.html>`_ and
replace anything that says ``pyramid.path`` with ``dotted_name_resolver``.

Supported python versions
-------------------------

::

    $ /Library/Frameworks/Python.framework/Versions/3.3/bin/tox
    ...
      py26: commands succeeded
      py27: commands succeeded
      py33: commands succeeded
      py34: commands succeeded
      pypy: commands succeeded
      congratulations :)

.. |Build Status| image:: https://travis-ci.org/msabramo/python_dotted_name_resolver.svg?branch=master
   :target: https://travis-ci.org/msabramo/python_dotted_name_resolver

.. |PyPI Version| image:: https://pypip.in/version/dotted_name_resolver/badge.svg
    :target: https://pypi.python.org/pypi/dotted_name_resolver/
    :alt: Latest Version
