callable-pip
============

``callable-pip`` patches over the wide use of ``pip.main()``

``pip.main()`` has never been a publicly supported API for ``pip``, but it has
often been used as such.

``callable-pip`` provides two public methods:

A drop-in replacement for ``pip.main()``::

    import callable_pip
    callable_pip.main()

A patch which adds ``pip.main()`` back to ``pip``, but which is dangerous and
known not to work on versions of ``pip`` which are not importable::

    import callable_pip
    callable_pip.dangerous_patch()
    ...
    pip.main()  # actually invokes callable_pip.main()


Usage
-----

If you are writing a python program, you can just use ``callable_pip.main()``
yourself.

If you have dependencies which use ``pip.main``, you can call
``callable_pip.dangerous_patch()`` yourself and it will usually work.

``dangerous_patch`` is so-named because it is *not* guaranteed to work on all
``pip`` versions and it is dangerous. Avoid it when possible.

Patching Without Control of Source
----------------------------------

You may be a consumer of packages which use ``pip.main()`` in a context where
you cannot modify or do not own the source. These techniques may help you.

More details on ``sitecustomize.py`` and ``.pth`` files can be found in the
Python documentation:
https://docs.python.org/3/library/site.html

Remember to remove these patches if you uninstall ``callable_pip``, or Python
will fail to start.

Applying the Patch With sitecustomize.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``sitecustomize.py`` is a file which is automatically loaded by the python
interpreter. It can exist anywhere in the ``PYTHONPATH``, including the current
directory.

Add a ``sitecustomize.py`` with the following content, or append it to an
existing ``sitecustomize.py``::

    import callable_pip
    callable_pip.dangerous_patch()

Applying the Patch With a .pth File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``.pth`` file can have any name you want, but must be installed in the
``site-packages`` directory.

Add a file, e.g. ``callable_pip.pth``, with the following content::

    import callable_pip; callable_pip.dangerous_patch()
