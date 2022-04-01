:py:mod:`mapping_helper_functions`
==================================

.. py:module:: mapping_helper_functions


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   mapping_helper_functions.get_polys_and_boxes
   mapping_helper_functions.sub_polybox
   mapping_helper_functions.get_intersections
   mapping_helper_functions.polygon_area



.. py:function:: get_polys_and_boxes(gc_lon1, gc_lat1, imask)


.. py:function:: sub_polybox(polybox, condition)


.. py:function:: get_intersections(polybox1, polybox2, kmax, cornermax)


.. py:function:: polygon_area(lats, lons, radius=6378137)

   Computes area of spherical polygon, assuming spherical Earth.
   Returns result in ratio of the sphere's area if the radius is specified.
   Otherwise, in the units of provided radius.
   Set radius to 1.0 to get square radians.
   lats and lons are in degrees.


