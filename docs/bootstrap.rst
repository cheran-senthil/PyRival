Infinite Recursion
******************

Infinite recursion can be achieved by using the :code:`pyrival.misc.bootstrap`
decorator

To use it you will need to make a few modifications to the recursive function:

 - Change all :code:`return` to :code:`yield`
 - Add :code:`yield` before recursive function calls


For example the following code

.. code-block:: python

   def factorial(n):
       if n == 0:
           return 1
       return n * factorial(n - 1)

   print(factorial(10))   # prints 3628800
   print(factorial(1000)) # exceeds recursion limit

will be changed to the following

.. code-block:: python

   import pyrival.misc

   @pyrival.misc.bootstrap
   def factorial(n):
       if n == 0:
           yield 1
       else:
           yield n * (yield factorial(n - 1))

   print(factorial(10))    # prints 3628800
   print(factorial(1000)   # prints 402387...000000
   print(factorial(10000)) # prints 284625...000000
