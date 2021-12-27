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
.. code-block:: sh

   pip install smart_inputs



Usage Examples
##############

String input with no extra validation.
*******************************************

.. code-block:: python
   :linenos:
   
   from smart_inputs import smart_input
   
   val = smart_input("Enter your name: ", cast=str)


String input with phone number regex validation.
******************************************************

.. code-block:: python
   :linenos:

   from smart_inputs import smart_input

   val = smart_input("Enter your phone number: ", cast=str, regex=r"^\d{3}-\d{3}-\d{4}$")


Integer input with default value.
**************************************

.. code-block:: python
   :linenos:

   from smart_inputs import smart_input

   val = smart_input("Enter your age: ", cast=int, default=18)


Integer input with a range.
***************************

.. code-block:: python
   :linenos:

   from smart_inputs import smart_input

   val = smart_input("Enter your age: ", cast=int, min_val=18, max_val=65)



Float input with a default value
*********************************

.. code-block:: python
   :linenos:

   from smart_inputs import smart_input

   val = smart_input("Enter your GPA: ", cast=float, min_val=0.0, max_val=4.0)



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
