:py:mod:`model_handling`
========================

.. py:module:: model_handling


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   model_handling.ModelTypes
   model_handling.ModelHandlerBase



Functions
~~~~~~~~~

.. autoapisummary::

   model_handling.get_model_handler
   model_handling.get_model_handlers



.. py:class:: ModelTypes

   Available model types
       

   .. py:attribute:: atmosphere
      :annotation: = atmosphere

      Identifier for atmospheric models.

      Note that there can be only one atmospheric model in a coupled run.


   .. py:attribute:: bottom
      :annotation: = bottom

      Identifier for bottom models as ocean or land models.

      In contrast to the atmosphere there can be several bottom models in a coupled run.


   .. py:attribute:: flux_calculator
      :annotation: = flux_calculator

      Reserved only for the flux_calculator.
          


   .. py:attribute:: other
      :annotation: = other

      Components, tools that are not coupled, as e.g. the int2lm tool.
          



.. py:function:: get_model_handler(global_settings, model)


.. py:function:: get_model_handlers(global_settings)


.. py:class:: ModelHandlerBase(model_type, global_settings, my_directory)

   Base class for all specific model handler.

   This constructor must be called in the constructor of the child class as e.g.
   `ModelHandlerBase.__init__(self, model_handling.ModelTypes.bottom, global_settings, my_directory)`

   :param global_settings:         Object containing the global settings
   :type global_settings:          class:`GlobalSettings` 

   :param my_directory:            Name of the model's input folder, usually model_domain, e.g. MOM5_Baltic. IMPORTANT: model names can only have for letters as e.g. MOM5, CCLM, GETM etc.
   :type my_directory:             str
                                   
   :param model_type:              Must be one of attributes of class `ModelTypes`
   :type model_type:               str

   .. py:method:: create_work_directory(self, work_directory_root, start_date, end_date)

      Method to perform model-specific steps for creating the work directory.

      This method is overwritten by the child class and will be called after 
      the work directory has been created and the content of the input folder has been copied to that work directory.

      It should typically do:

      * Copy the executable(s) to the work directory (not into subfolders)

      * Apply current start date and end date to input files

      :param work_directory_root:     Is the local work directory common to all models, thus it is one lvel above my_directory
      :type work_directory_root:      str

      :param start_date:              Start date of the current working period, format YYYYMMDD, e.g. 20220325 for the 25th of March 2022
      :type start_date:               str 
                                      
      :param end_date:                End date of the current working period, format YYYYMMDD, e.g. 20220325 for the 25th of March 2022
      :type end_date:                 str


   .. py:method:: check_for_success(self, work_directory_root, start_date, end_date)

      Method to if model run was successful or not.

      This method is overwritten by the child class and will be called after 
      the MPI task has finished.

      It should typically do:

      * Check for the existence of some specific output files.

      :param work_directory_root:     Is the local work directory common to all models, thus it is one lvel above my_directory
      :type work_directory_root:      str

      :param start_date:              Start date of the current working period, format YYYYMMDD, e.g. 20220325 for the 25th of March 2022
      :type start_date:               str 
                                      
      :param end_date:                End date of the current working period, format YYYYMMDD, e.g. 20220325 for the 25th of March 2022
      :type end_date:                 str

      :return:                        `True` if model has finished successfully, `False` otherwise
      :rtype:                         bool        


   .. py:method:: move_results(self, work_directory_root, start_date, end_date)


   .. py:method:: grid_convert_to_SCRIP(self)


   .. py:method:: get_model_executable(self)


   .. py:method:: get_num_threads(self)



