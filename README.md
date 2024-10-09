# python_dotted_name_resolver

[![Build status][Build status image]][Build status link]
[![Latest version][Latest version image]][Latest version link]

[DottedNameResolver] and other stuff lifted from [pyramid.path] from the
wonderful [Pyramid] web framework.

## A few quick examples of usage

``` python
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
```

## Documentation

For detailed documentation, see [the documentation for
pyramid.path](http://docs.pylonsproject.org/projects/pyramid/en/latest/api/path.html)
and replace anything that says `pyramid.path` with
`dotted_name_resolver`.

## Supported python versions

```shell
$ tox
    py39-zope.interface0: OK (3.89=setup[3.67]+cmd[0.22] seconds)
    py39-zope.interface1: OK (1.46=setup[1.23]+cmd[0.23] seconds)
    py310-zope.interface0: OK (0.87=setup[0.64]+cmd[0.22] seconds)
    py310-zope.interface1: OK (0.84=setup[0.61]+cmd[0.23] seconds)
    py311-zope.interface0: OK (0.88=setup[0.67]+cmd[0.21] seconds)
    py311-zope.interface1: OK (0.86=setup[0.63]+cmd[0.22] seconds)
    py312-zope.interface0: OK (2.28=setup[2.04]+cmd[0.24] seconds)
    py312-zope.interface1: OK (2.48=setup[2.22]+cmd[0.26] seconds)
    congratulations :) (13.66 seconds)
```

[Build status image]: https://github.com/msabramo/python_dotted_name_resolver/actions/workflows/python-package.yml/badge.svg
[Build status link]: https://github.com/msabramo/python_dotted_name_resolver/actions/workflows/python-package.yml
[Latest version image]: https://img.shields.io/pypi/v/dotted_name_resolver.svg
[Latest version link]: https://pypi.python.org/pypi/dotted_name_resolver/
[DottedNameResolver]: http://docs.pylonsproject.org/projects/pyramid/en/latest/api/path.html#pyramid.path.DottedNameResolver
[pyramid.path]: http://docs.pylonsproject.org/projects/pyramid/en/latest/api/path.html
[Pyramid]: http://docs.pylonsproject.org/projects/pyramid/
