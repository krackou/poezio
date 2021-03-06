Installing poezio
=================

.. important:: Python 3.4 or above is **required**

poezio in the GNU/Linux distributions
-------------------------------------

As far as I know, Poezio is available in the following distributions, you just
have to install it by using the package manager of the distribution, if you're
using one of these.

- *Archlinux*: A poezio_ and poezio-git_ packages are in AUR (use your favourite
    AUR wrapper to install them)
- *Gentoo*: `Sekh’s overlay`_ contains everything required to build poezio
    (sleekxmpp, dnspython, and poezio)
- *Fedora*: The poezio package was out of date for a long time in Fedora, but
    now thanks to Casper, there is an `up-to-date package`_ in the repos since F19.
- *Debian*: Use an other distro. (or make a package, we can provide help :) )

(If another distribution provides a poezio package, please tell us and we will
add it to the list)

Install from source
-------------------

Stable version
~~~~~~~~~~~~~~

`Stable version`_ packages are available in standalone (dependencies provided)
and poezio-only packages (both with prebuilt html doc for convenience).

Those versions are also available on pypi_ (using pip3, for example), and it is
recommended to install them this way if you absolutely want to **install** poezio
and your distribution provides no package.

Development version
~~~~~~~~~~~~~~~~~~~

The stable versions of poezio are more like snapshots of states of
development we deem acceptable. There is always an incentive to
use the development version, like new features, bug fixes, and more
support. Therefore, you might want to use the git version.

.. code-block:: bash

    git clone git://git.poez.io/poezio
    cd poezio

"""""""
General
"""""""

Poezio is a python3.4 (and above)-only application, so you will first need that.

You will also need the python3-devel package or equivalent, and make, in order
to compile the poezio C module. Then you can run ``make`` to build it.
If you downloaded the standalone stable package, you are finished here and can skip
to :ref:`running poezio <poezio-run-label>`.

Poezio depends on two libraries:

- aiodns_
- slixmpp_

.. versionchanged:: 0.9


Additionally, it needs *python3-setuptools*, which is required for proper python
packaging management.

.. note:: We provide a script ``update.sh`` that creates a virtualenv and
          downloads all the required and optional dependencies inside it.
          we recommend using it with the git version of poezio, in order
          to keep everything up-to-date.

If you don’t want to use the update script for whatever reason, install the
following dependencies by hand; otherwise, skip to the
`installation part <poezio-install-label>`.


""""""""
slixmpp
""""""""

Poezio depends on slixmpp, a non-thread fork of the SleekXMPP library.

.. code-block:: bash

    git clone git://git.louiz.org/slixmpp
    python3 setup.py install --user


""""""
aiodns
""""""

The aiodns is required in order to properly resolve XMPP domains (with SRV records).


.. code-block:: bash

    pip install --user aiodns

This will also install pycares, which aiodns uses.


.. _poezio-install-label:

Installation
~~~~~~~~~~~~

.. note::

    The update.sh + launch.sh method is the recommended way of using and upgrading
    the devel version of poezio. Installing should only be done with stable versions.
    And preferably using your distribution’s package manager.


If you skipped the installation of the dependencies and you only want to run
poezio without a system-wide install, do, in the :file:`poezio` directory:

.. code-block:: bash

    ./update.sh


If you really want to install it, run as root (or sudo in ubuntu or whatever):

.. code-block:: bash

    make install


.. _poezio-run-label:

Running
~~~~~~~

If you didn’t install poezio, you can run it from the source directory
with:

.. code-block:: bash

    ./launch.sh


If you did, it should be in he ``$PATH`` as ``poezio``, so run:

.. code-block:: bash

    poezio

.. _Sekh’s overlay: https://github.com/sekh/sekh_overlay
.. _stable sources: https://dev.louiz.org/project/poezio/download
.. _slixmpp: https://dev.louiz.org/projects/slixmpp
.. _aiodns: https://github.com/saghul/aiodns
.. _poezio: https://aur.archlinux.org/packages/poezio/
.. _poezio-git: https://aur.archlinux.org/packages/poezio-git/
.. _up-to-date package: https://apps.fedoraproject.org/packages/poezio
.. _pypi: https://pypi.python.org/pypi/poezio
