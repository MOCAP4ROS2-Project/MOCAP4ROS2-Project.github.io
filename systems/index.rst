Systems
#######

.. list-table::
   :header-rows: 1

   * - System
     - Package
     - Connection
     - Data
   * - :doc:`OptiTrack <optitrack>` (Motive)
     - ``mocap4r2_optitrack_driver``
     - NatNet 3.0–4.5, multicast or unicast; official SDK or open implementation
     - markers, rigid bodies, skeletons
   * - :doc:`Vicon <vicon>` (Nexus, Tracker, Shogun)
     - ``mocap4r2_vicon_driver``
     - DataStream SDK 1.13 (included)
     - markers, subjects, segments
   * - :doc:`Qualisys <qualisys>` (QTM)
     - ``mocap4r2_qualisys_driver``
     - RT protocol, Qualisys C++ SDK (included), TCP or UDP
     - markers, 6DOF bodies, skeletons
   * - :doc:`Gazebo <gazebo>`
     - ``mocap4r2_gz_plugin``
     - plugin of the world; ROS output or simulated Motive
     - markers, rigid bodies
   * - :doc:`Simulated <simulated>`
     - ``mocap4r2_sim_driver``
     - none
     - markers, rigid bodies with noise, occlusions and drops

All systems share the parameters ``frame_id``, ``publish_markers``,
``publish_rigid_bodies``, ``publish_skeletons``, ``publish_tf``, ``tf_prefix``,
``qos.reliability``, ``qos.depth`` and ``autostart`` (``none``, ``configure`` — the
default: connect and wait for START — or ``activate``).

.. toctree::
   :maxdepth: 1

   optitrack
   vicon
   qualisys
   gazebo
   simulated
