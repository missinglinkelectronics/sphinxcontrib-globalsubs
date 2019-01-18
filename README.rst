*************************************
Sphinx Global Substitutions Extension
*************************************

This extension adds support for global substitutions to ``conf.py``. One of the
main use cases are central abbreviation lists, but any valid reST markup can be
substituted.


Installation
============

Just install via ``pip``:

.. code-block:: console

   $ pip install sphinxcontrib-globalsubs

Then add the module ``sphinxcontrib.globalsubs`` to the
``extensions`` list in your ``conf.py``.


Usage
=====

Add global substitutions via the ``global_substitutions`` dictionary in your
``conf.py``:

.. code-block:: python

   global_substitutions = {
       'sub': 'substitution',
       'tla': ':abbr:`TLA (Three Letter Acronym)`',
       'img': '.. image:: img.png'
   }

Global substitutions are processed after default substitutions like
``|release|``, ``|version|`` and ``|today|``, but before any other
substitutions in source files (i.e. global substitutions can be overriden).
