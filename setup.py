# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = '''
Adds support for global substitutions to ``conf.py``.
'''

requires = ['Sphinx>=7.0']

setup(
    name='sphinxcontrib-globalsubs',
    version='1.0.0',
    url='https://github.com/missinglinkelectronics/sphinxcontrib-globalsubs',
    download_url='https://pypi.org/project/sphinxcontrib-globalsubs',
    license='BSD',
    author='Stefan Wiehler',
    author_email='sphinx_contribute@missinglinkelectronics.com',
    description='Sphinx global substitutions extension',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Framework :: Sphinx :: Extension',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    python_requires='~=3.4',
    namespace_packages=['sphinxcontrib'],
)
