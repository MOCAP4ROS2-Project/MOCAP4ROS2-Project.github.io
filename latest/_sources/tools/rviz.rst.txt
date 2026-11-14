RViz
####

.. code-block:: console

   $ ros2 launch mocap4r2_marker_viz marker_viz.launch.yaml namespace:=lab

``mocap4r2_marker_viz`` turns the data of a system into ``mocap_viz``
(``MarkerArray``): labeled markers (green), unlabeled (white), occluded (red,
transparent), rigid bodies as axes with their names ("lost" when not tracked) and
skeletons as bones and joints. It is throttled to ``max_rate`` (30 Hz) because mocap
rates are higher than what RViz can draw, and clears the scene when no data arrives
for ``stale_timeout`` seconds. Enable ``publish_tf`` in the driver to also see every
rigid body as a TF frame.
