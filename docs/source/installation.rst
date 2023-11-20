Installation
============

Prerequisites
-------------



.. table::  Table example.

            +--------+---------+-----+-----------+-----------+----------+
            |                        |        Linux architectures       |
            |                        +-----------+-----------+----------+
            |     Python version     |   x86_64  |  aarch64  | arm32v7l |
            +========================+===========+===========+==========+
            |           3.7          | on demand | on demand |    Yes   |
            +------------------------+-----------+-----------+----------+

The SDK needs some packages to be installed in order to be able to run:

.. table::  SDK's requirements.

            +----------------------+--------------+
            | Package              | Version      |
            +======================+==============+
            | numpy                | >= 1.16.3    |
            +----------------------+--------------+
            | opencv-python        | >= 3.4.16.59 |
            +----------------------+--------------+
            | rknn / rknnlite      | >= 1.7.1     |
            +----------------------+--------------+
            | rockchipinferenceapi | >= 0.3.1     |
            +----------------------+--------------+

.. note:: **SDK** will be provided by Servihabitat in wheel format.


SDK installation via pip
------------------------

To install cron_py using pip

.. code-block:: console

   (.venv) $ pip install cron_py
