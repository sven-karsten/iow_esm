:py:mod:`machine_settings_hlrn`
===============================

.. py:module:: machine_settings_hlrn


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   machine_settings_hlrn.machinefile_line
   machine_settings_hlrn.get_node_list



Attributes
~~~~~~~~~~

.. autoapisummary::

   machine_settings_hlrn.mpi_run_command
   machine_settings_hlrn.mpi_n_flag
   machine_settings_hlrn.bash_get_rank
   machine_settings_hlrn.python_get_rank
   machine_settings_hlrn.use_mpi_machinefile
   machine_settings_hlrn.resubmit_command


.. py:data:: mpi_run_command
   :annotation: = mpirun -configfile mpmd_file

   

.. py:data:: mpi_n_flag
   :annotation: = -n

   

.. py:data:: bash_get_rank
   :annotation: = my_id=${PMI_RANK}

   

.. py:data:: python_get_rank
   :annotation: = my_id = int(os.environ["PMI_RANK"])

   

.. py:data:: use_mpi_machinefile
   :annotation: = -machine machine_file

   

.. py:function:: machinefile_line(node, ntasks)


.. py:function:: get_node_list()


.. py:data:: resubmit_command
   :annotation: = sbatch jobscript

   

