:py:mod:`parse_global_settings`
===============================

.. py:module:: parse_global_settings


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   parse_global_settings.GlobalSettings




.. py:class:: GlobalSettings(root_dir, input_name='')

   Class that contains the variables of global_settings.py as attributes.

   Attributes will be all that are present in global_settings.py.
       
   Additionally there will be `root_dir` which is the memorized path of root directory and
   `attempt_handler_obj_file`. The latter is the file which is used to serialize the current state of the attempt_handler attribute.  
   IMPORTANT: If you want to start from scratch, you have to remove this file.

   :param root_dir:        Path to the root directory
   :type root_dir:         str
           
   :param global_settings: Path to the global_settings.py file, relative to root_dir, default "input/global_settings.py" 
   :type global_settings:  str

   .. py:method:: serialize_attempt_handler(self)

      Serializes the attempt_handler object into a binary file.

      This function is used to store the state of the attempt_handler object at the end of a run.
      Such it can be restored when starting a new run.



   .. py:method:: deserialize_attempt_handler(self)

      Deserializes the attempt_handler object from a binary file.

      If a file named as attempt_handler_obj_file exists, the attempt_handler object is restore from that.
      If there is not such a file, nothing is done here and the attempt_handler object is initialized as implemented in its contructor.




