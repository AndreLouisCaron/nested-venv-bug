nested-venv-bug
===============

Minimal project to demonstrate strange issue when creating nested virtual
environments inside a test suite run by Tox_ against Python 3.5.

.. _Tox: https://tox.readthedocs.org/en/latest/

test.sh
-------

The ``test.sh`` script is a simple Bash script that creates a ``foo`` virtual
environment, activates it and then creates a ``bar`` environment from there,
activates that and then installs Flask_.

Here are the steps to run::

  $ rm -rf foo/ bar/
  $ ./test.sh

This works as expected.  Installing packages works as expected (i.e. the
package is installed in the ``bar`` virtual environment).

.. _Flask: http://flask.pocoo.org/

test.py
-------

The ``test.py`` script is a plain implementation of ``test.sh`` directly in
Python.

Here are the steps to run::

  $ rm -rf foo/ bar/
  $ ./test.py

The results are the same (but output is captured and is not displayed).

test-for-tox.py
---------------

The ``test-for-tox.py`` script creates a single ``bar`` virtual environment,
activates it and then attempts to install a package.

Since Tox runs the script inside a virtual environment it created, then that
environment serves as the ``foo`` environment in ``foo.sh`` and ``foo.py``.

Here are the steps to run::

  $ rm -rf foo/ bar/
  $ tox

AFAICT, this *should* be equivalent to the other two scripts.

However, this script fails with this error::

  FileNotFoundError: [Errno 2] No such file or directory: './bar/bin/pip'

When we dig a bit deeper, we notice that the ``./bar/bin/activate`` is **not**
executable and that ``./bar/bin/pip`` is indeed missing.

License
-------

All code in this project is placed in the public domain.
