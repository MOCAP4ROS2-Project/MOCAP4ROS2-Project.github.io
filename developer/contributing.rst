Contributing
############

Repositories
************

.. list-table::
   :header-rows: 1

   * - Repository
     - Packages
   * - :repo:`mocap4r2_msgs`
     - ``mocap4r2_interfaces``
   * - :repo:`mocap4r2`
     - ``mocap4r2_control``, ``mocap4r2_sim_driver``, ``mocap4r2_marker_viz``,
       ``mocap4r2_robot_gt``, ``mocap4r2_gt_tools``, ``mocap4r2_motion_tools``,
       ``mocap4r2_tools``
   * - :repo:`mocap4ros2_optitrack`
     - ``mocap4r2_optitrack_driver``
   * - :repo:`mocap4ros2_vicon`
     - ``mocap4r2_vicon_driver``
   * - :repo:`mocap4ros2_qualisys`
     - ``mocap4r2_qualisys_driver``
   * - :repo:`mocap4ros2_gazebo`
     - ``mocap4r2_gz_plugin``

One branch (``rolling``) builds on Humble, Jazzy, Kilted, Lyrical and Rolling; the CI
of every repository builds and tests the five distributions (the OptiTrack repository
also with the official NatNet SDK).

Pull requests
*************

* Open an issue first for anything beyond a small fix.
* Add tests for the behaviour you change: situations, edge values and sequences, not
  only the happy path.
* Code style: ``ament_uncrustify`` (the Jazzy and newer version), ``ament_cpplint``,
  ``ament_flake8``; every file has the Apache 2.0 header.
* Sign off your commits (``git commit -s``).
