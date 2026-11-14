Simulated system
################

``mocap4r2_sim_driver`` produces synthetic rigid bodies and markers from an
acquisition thread, like a real SDK. It is the quickest way to try the tools, write
applications or test a pipeline in CI.

.. code-block:: console

   $ ros2 launch mocap4r2_sim_driver sim_driver.launch.py autostart:=activate

.. list-table::
   :header-rows: 1

   * - Parameter
     - Default
     - Meaning
   * - ``rate``
     - 120
     - frame rate, Hz
   * - ``bodies``
     - ``[robot, wand]``
     - rigid bodies; each one configured in ``bodies_config.<name>.{motion, center,
       radius, period}`` (``circle``, ``figure8`` or ``static``)
   * - ``markers_per_body``
     - 4
     - 0 to 6 markers in an asymmetric pattern
   * - ``unlabeled_markers``
     - 0
     - random unlabeled markers per frame
   * - ``noise``
     - 0.0005
     - marker noise std, metres
   * - ``occlusion_probability`` / ``occlusion_duration``
     - 0 / 0.2
     - chance per frame and body of starting an occlusion, and its length (s)
   * - ``frame_drop_probability``
     - 0
     - chance of dropping a frame (shows as a gap in ``frame_number``)
   * - ``latency``
     - 0.004
     - simulated system latency, seconds
   * - ``seed``
     - 42
     - random seed (the scene is deterministic)
