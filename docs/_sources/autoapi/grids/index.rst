:py:mod:`grids`
===============

.. py:module:: grids


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   grids.Grid
   grids.IntersectionGrid
   grids.GridManager




.. py:class:: Grid(title=None, from_grid=None, **kwargs)

   .. py:method:: reconfigure(self, **kwargs)


   .. py:method:: read(self, file_name)


   .. py:method:: write(self, file_name)



.. py:class:: IntersectionGrid(grid1, grid2, **kwargs)

   Bases: :py:obj:`Grid`


.. py:class:: GridManager(grid1, grid2, exchange_grid=None)

   .. py:method:: prepare_exchange_grid(self, src_for_exchange_grid)


   .. py:method:: write_remapping(self, file_name, src, dst)



