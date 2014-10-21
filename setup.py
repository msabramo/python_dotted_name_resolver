import os
import sys

from setuptools import setup, find_packages

py_version = sys.version_info[:2]

PY3 = py_version[0] == 3

if PY3:
    if py_version < (3, 2):
        raise RuntimeError('On Python 3, we require Python 3.2 or better')
else:
    if py_version < (2, 6):
        raise RuntimeError('On Python 2, we require Python 2.6 or better')

here = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(here, 'README.rst')) as f:
        README = f.read()
    with open(os.path.join(here, 'CHANGES.txt')) as f:
        CHANGES = f.read()
except IOError:
    README = CHANGES = ''

install_requires=[
    'setuptools',
]

docs_extras = [
    'Sphinx',
    'docutils',
    'repoze.sphinx.autointerface',
]

testing_extras = [
    'pytest',
    'pytest-cov',
]

setup(
    name='dotted_name_resolver',
    version='0.0',
    description='DottedNameResolver and other stuff lifted from pyramid.path',
    long_description=README + '\n\n' +  CHANGES,
    author="Marc Abramowitz",
    author_email="marc@marc-abramowitz.com",
    url="https://github.com/msabramo/python_dotted_name_resolver",
    license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    extras_require={
        'testing': testing_extras,
        'docs': docs_extras,
    },
    tests_require=['pytest'],
    test_suite="dotted_name_resolver.tests",
)
