:py:mod:`machine_settings_haumea`
=================================

.. py:module:: machine_settings_haumea


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   machine_settings_haumea.machinefile_line
   machine_settings_haumea.get_node_list



Attributes
~~~~~~~~~~

.. autoapisummary::

   machine_settings_haumea.mpi_run_command
   machine_settings_haumea.mpi_n_flag
   machine_settings_haumea.bash_get_rank
   machine_settings_haumea.python_get_rank
   machine_settings_haumea.use_mpi_machinefile


.. py:data:: mpi_run_command
   :annotation: = mpirun --app mpmd_file

   

.. py:data:: mpi_n_flag
   :annotation: = -np

   

.. py:data:: bash_get_rank
   :annotation: = my_id=${OMPI_COMM_WORLD_RANK}

   

.. py:data:: python_get_rank
   :annotation: = my_id = int(os.environ["OMPI_COMM_WORLD_RANK"])

   

.. py:data:: use_mpi_machinefile
   :annotation: = --oversubscribe -hostfile machine_file

   

.. py:function:: machinefile_line(node, ntasks)


.. py:function:: get_node_list()


