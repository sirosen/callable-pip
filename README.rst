callable-pip
============

.. warning::

    Use at your own risk.

``callable-pip`` provides a drop-in replacement for ``pip.main()`` and support
for monkey-patching ``pip.main`` via a known-dangerous method.

``pip.main()`` has never been a publicly supported API for ``pip``, but it has
often been used as such. This tiny package is meant to cover the gap and ease
people's transitions to new usage.

Drop-in Replacement for pip.main
--------------------------------

This usage is *always guaranteed to work* on any supported python version with
any functioning version of ``pip``.

Instead of ``pip.main(...)``, use this method instead::

    import callable_pip
    callable_pip.main('install', '--upgrade', 'setuptools')

If you are writing a python program, you can just use ``callable_pip.main()``
yourself. This is the only guaranteed-safe usage.

Patching pip.main
-----------------

``callable-pip`` provides a patch which adds ``pip.main()`` back to ``pip``,
but which is dangerous and known not to work on some versions of ``pip``::

    import callable_pip
    callable_pip.dangerous_patch()
    ...
    import pip
    pip.main('--version')  # actually invokes callable_pip.main()

If you have dependencies which use ``pip.main``, you can call
``callable_pip.dangerous_patch()`` yourself and it will *usually* work.

``dangerous_patch`` is so-named because it is *not* guaranteed to work on all
``pip`` versions and it is dangerous. Avoid it when possible.

Patching Without Control of Source
----------------------------------

You may be a consumer of packages which use ``pip.main()`` in a context where
you cannot modify or do not own any of the source.
These techniques may help you.

More details on ``sitecustomize.py`` and ``.pth`` files can be found in the
Python documentation:
https://docs.python.org/3/library/site.html

Remember to remove these patches if you uninstall ``callable_pip``, or Python
will fail to start.

Applying the Patch With sitecustomize.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``sitecustomize.py`` can exist anywhere in the ``PYTHONPATH``, including the
directory where python is invoked.

Add a ``sitecustomize.py`` with the following content, or append it to an
existing ``sitecustomize.py``::

    import callable_pip
    callable_pip.dangerous_patch()

Applying the Patch With a .pth File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``.pth`` file can have any name you want, but must be installed in the
``site-packages`` directory. It may therefore require root or other elevated
privileges to add.

Add a file, e.g. ``callable_pip.pth``, with the following content::

    import callable_pip; callable_pip.dangerous_patch()

Documentation
=============

All documentation is in this readme doc.

Bug and Issue Reports
=====================

Submit all bug reports and issues here:
https://github.com/sirosen/callable-pip/issues

Changelog
=========

2.0.0
-----

Update to ``pyproject.toml`` with ``flit-core`` for package builds.

Defer import of ``subprocess`` until it is needed.

1.0.0
-----

Improved docs, releasing as v1.0 Production after some testing and validation.
No code changes from v0.1.0

0.1.0
-----

Initial version
