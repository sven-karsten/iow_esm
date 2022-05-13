:py:mod:`parallelize_mappings_helpers`
======================================

.. py:module:: parallelize_mappings_helpers


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   parallelize_mappings_helpers.get_exchange_grid_task_vector
   parallelize_mappings_helpers.add_exchange_grid_task_vector
   parallelize_mappings_helpers.get_halo_cells
   parallelize_mappings_helpers.sort_exchange_grid
   parallelize_mappings_helpers.update_remapping
   parallelize_mappings_helpers.update_remapping_from_model_to_exchange
   parallelize_mappings_helpers.update_remapping_from_exchange_to_model
   parallelize_mappings_helpers.write_remap_file
   parallelize_mappings_helpers.update_regridding
   parallelize_mappings_helpers.visualize_domain_decomposition



.. py:function:: get_exchange_grid_task_vector(global_settings, model, model_tasks, grid, work_dir)


.. py:function:: add_exchange_grid_task_vector(global_settings, model, eg_tasks, grid, work_dir)


.. py:function:: get_halo_cells(global_settings, model, grid, work_dir)


.. py:function:: sort_exchange_grid(global_settings, model, grid, halo_cells, work_dir)


.. py:function:: update_remapping(global_settings, model, grid, work_dir)


.. py:function:: update_remapping_from_model_to_exchange(global_settings, model, grid, work_dir)


.. py:function:: update_remapping_from_exchange_to_model(global_settings, model, grid, work_dir)


.. py:function:: write_remap_file(file_name, src_grid_name, dst_grid_name, src_grid_size=None, dst_grid_size=None, src_grid_corners=None, dst_grid_corners=None, src_grid_rank=None, dst_grid_rank=None, num_links=None, num_wgts=None, src_grid_dims=None, dst_grid_dims=None, src_grid_center_lat=None, dst_grid_center_lat=None, src_grid_center_lon=None, dst_grid_center_lon=None, src_grid_imask=None, dst_grid_imask=None, src_grid_area=None, dst_grid_area=None, src_grid_frac=None, dst_grid_frac=None, src_address=None, dst_address=None, remap_matrix=None)


.. py:function:: update_regridding(global_settings, model, grid, work_dir)


.. py:function:: visualize_domain_decomposition(global_settings, model, grid, model_tasks, eg_tasks=None, halo_cells=None)


