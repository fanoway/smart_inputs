.. smart_inputs documentation master file, created by
   sphinx-quickstart on Sun Dec 26 16:13:02 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to smart_inputs's documentation!
========================================

Smarter methods to get user input in python including defaults, regex and type validation. Requests for rentry are handled automatically if the validation fails.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   smart_inputs

Installation
############
.. code-block::

   pip install smart_inputs



Usage Examples
##############


String input with regex to rqeuire a capitalised word
******************************************************

.. code-block:: python
   :linenos:

   from smart_inputs import string_input

   string = string_input('What is your name? ', regex="[A-z][a-z]+")


Integer input with a minimum value
**********************************

.. code-block:: python
   :linenos:

   from smart_inputs import int_input

   integer = int_inpuT('How old are you ? ', min_val = 0)


Float input with a default value
*********************************

.. code-block:: python
   :linenos:

   from smart_inputs import float_input

   float = float_input('Whats your GPA? ', min_val = 0, max_val = 4.0, default = 2.5)



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
