:py:mod:`attempt_handler_example`
=================================

.. py:module:: attempt_handler_example


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   attempt_handler_example.MyAttemptHandler




.. py:class:: MyAttemptHandler(root='.')

   Class that handles your attempts.

   The name of the class is arbitrary

   Mandatory attributes: `next_attempt` which represents your next attempt, type must be convertable by str() function to string, typically a string or an integer, if all attempts are exhausted and you want to stop this must be set to None.
                                   
   Class can have arbitrarily more optional attributes. 
   However, all attributes must be serializable by the pickle library, see https://docs.python.org/3/library/pickle.html.
   The serialization into a file is necessary to store the state of the attempt handler over several jobs.
   IMPORTANT: If you want to start from scratch, you have to remove such files, which are sored as <run_name>_attempt_handler.obj in the root directory.

   Parameters can be arbitrary. In this example:

   :param root:        Path to the root directory
   :type root:         str     
       

   .. py:method:: prepare_attempt(self, **kwargs)

      Mandatory method to prepare the attempt.

      Do whatever is necessary to set up the next attempt, e.g. manipulating input files.

      :Keyword Arguments:

      * **start_date** (*int*) --
        Start date of the current job in format YYYMMDD
      * **end_date** (*int*) --
        End date of the current job in format YYYMMDD  
              


   .. py:method:: evaluate_attempt(self, crashed, **kwargs)

      Mandatory method to evaluate the attempt.

      In this method the setting of the next_attempt should typically happen, e.g. incrementation.
      Important: If all attempts are exhausted, next_attempt must be set tot `None`.
      Important: If model has crashed, this function should return False otherwise following steps are ill-defined.

      :param crashed:         `True`, if the model has crashed, `False`, otherwise
      :type crashed:          bool   

      :Keyword Arguments:

      * **start_date** (*int*) --
        Start date of the current job in format YYYMMDD
      * **end_date** (*int*) --
        End date of the current job in format YYYMMDD          

      :return:                `True`, if attempt is accepted (work will be copied to output, hotstart folder is created), `False`, if attempt is not accepted (work will not be copied to output, no hotstart folder is created)      
      :rtype:                 bool



