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

   Method to get a single model handler.

   This method imports the model-specific handling module `model_handling_ABCD.py`
   where `ABCD` is a four letter acronym of the model.

   :param global_settings:         Object containing the global settings
   :type global_settings:          class:`GlobalSettings` 

   :param model:                   Name of the model's input folder, usually model_domain, e.g. MOM5_Baltic. IMPORTANT: model names can only have four letters as e.g. MOM5, CCLM, GETM etc.
   :type model:                    str
                                   
   :return:                        Specific model handler object
   :rtype:                         class:`ModelHandler`      


.. py:function:: get_model_handlers(global_settings)

   Method to get handlers for all models that have input folders.

   This method checks the input folder and creates model handler objects for found models. 
   If there is one atmospheric model and at least one bottom model the run will be interpreted as a coupled run.
   In that case the flux_calculator is added to the models.

   :param global_settings:         Object containing the global settings
   :type global_settings:          class:`GlobalSettings` 
                                   
   :return:                        Dictionary of specific model handler objects. The keys of the dictionary are the names of the input folders
   :rtype:                         dict    


.. py:class:: ModelHandlerBase(model_type, global_settings, my_directory)

   Base class for all specific model handler.

   This constructor must be called in the constructor of the child class as e.g.
   `ModelHandlerBase.__init__(self, model_handling.ModelTypes.bottom, global_settings, my_directory)`
   The child class must be implmented as `ModelHandler` in a python module called `model_handling_ABCD.py` 
   where `ABCD` is a four letter acronym of your model.

   :param global_settings:         Object containing the global settings
   :type global_settings:          class:`GlobalSettings` 

   :param my_directory:            Name of the model's input folder, usually model_domain, e.g. MOM5_Baltic. IMPORTANT: model names can only have four letters as e.g. MOM5, CCLM, GETM etc.
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

      Method to check if model run was successful or not.

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

      Method to move results from work to output folder.

      This method is overwritten by the child class and will be called after 
      the check_for_success method has returned `True`.

      It should typically do:

      * Move all files you want to keep that are used or produced by your model.

      :param work_directory_root:     Is the local work directory common to all models, thus it is one lvel above my_directory
      :type work_directory_root:      str

      :param start_date:              Start date of the current working period, format YYYYMMDD, e.g. 20220325 for the 25th of March 2022
      :type start_date:               str 
                                      
      :param end_date:                End date of the current working period, format YYYYMMDD, e.g. 20220325 for the 25th of March 2022
      :type end_date:                 str      


   .. py:method:: grid_convert_to_SCRIP(self)


   .. py:method:: get_model_executable(self)

      Method to get the name of the model's excutable.

      This method is overwritten by the child class and will be called when the MPI run script is created.

      It should typically do:

      * Return the name of the executable that is located in your work directory after create_work_directory has been called. 
                                                          
      :return:                        Name of the excutable, e.g. "fms_MOM_SIS.x"
      :rtype:                         str


   .. py:method:: get_num_threads(self)

      Method to get the number of threads the model is using.

      This method is overwritten by the child class and will be called when the paralleization layout is created.

      It should typically do:

      * Return the number of threads using e.g. settings in the model's input files. 
                                      
      :return:                        Number of used threads
      :rtype:                         int    



