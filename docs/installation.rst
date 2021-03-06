.. _installation:


Installation
============

PIP installation from the test PyPI node
****************************************

.. code-block:: bash

  pip install esgissue-client


Installation from GitHub
************************

1. Create a new directory:

.. code-block:: bash

  mkdir esdoc-errata-client
  cd esdoc-errata-client

2. Clone `our GitHub project <http://github.com/ES-DOC/esdoc-errata-client/>`_:

.. code-block:: bash

  git init
  git clone git@github.com:ES-DOC/esdoc-errata-client.git@master

3. Run the ``setup.py``:

.. code-block:: bash

  python setup.py install


4. The ``esgissue`` command-line is ready.


Dependencies
************

``esgissue`` uses the following basic Python libraries includes in Python 2.5+. Please make sure your Python
environment includes the following:

- `os <https://docs.python.org/2/library/os.html>`_,

- `sys <https://docs.python.org/2/library/sys.html>`_,

- `re <https://docs.python.org/2/library/re.html>`_,

- `logging <https://docs.python.org/2/library/logging.html>`_

- `argparse <https://docs.python.org/2/library/argparse.html>`_

- `ConfigParser <https://docs.python.org/2/library/configparser.html>`_

- `datetime <https://docs.python.org/2/library/datetime.html>`_

- `uuid <https://docs.python.org/2/library/uuid.html>`_

- `string <https://docs.python.org/2/library/string.html>`_

- `json <https://docs.python.org/2/library/json.html>`_

``esgissue`` requires the following libraries not included in most Python distributions:

- `jsonschema <https://pypi.python.org/pypi/jsonschema>`_

- `requests <https://pypi.python.org/pypi/requests/2.11.1>`_
