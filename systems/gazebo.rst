Gazebo
######

``mocap4r2_gz_plugin`` (Jazzy and newer) is a world plugin that simulates a motion
capture room: it reads the pose of the links you choose, adds markers, and streams the
frames

* as a MOCAP4ROS2 system (``output: ros``), with simulation time, or
* as **OptiTrack Motive** (``output: natnet``): the real OptiTrack driver connects to
  Gazebo exactly as it would to Motive. Useful to test a whole setup, including the
  driver and its network configuration, before going to the lab.

.. code-block:: console

   $ ros2 launch mocap4r2_gz_plugin mocap_room.launch.yaml

Configuration (in the world SDF):

.. code-block:: xml

   <plugin filename="mocap4r2_gz_plugin" name="mocap4r2_gz_plugin::MocapSystem">
     <output>ros</output>          <!-- or natnet -->
     <rate>120</rate>
     <noise>0.0003</noise>         <!-- marker noise std, metres -->
     <dropout>0.0</dropout>        <!-- probability of losing a body in a frame -->
     <autostart>activate</autostart>
     <frame_id>mocap</frame_id>
     <rigid_body name="robot" link="my_robot::base_link">
       <offset>0 0 0.3 0 0 0</offset>   <!-- body frame in the link frame -->
       <marker name="front">0.12 0 0.02</marker>
       <marker name="left">-0.06 0.08 0.02</marker>
       <marker name="right">-0.06 -0.06 0.04</marker>
     </rigid_body>
   </plugin>

With ``output: natnet``, ``natnet_address``, ``natnet_command_port``,
``natnet_data_port``, ``natnet_multicast`` and ``up_axis`` (``y`` like Motive by
default) configure the simulated Motive.

The plugin does not publish while the simulation is paused, restarts its frame numbers
when the simulation is reset, and stamps the data with the simulation time.

Demos
*****

``mocap4r2_gz_demos`` (Jazzy and newer) has two ready-made scenarios, which also open
RViz (``rviz:=false`` to skip it):

.. code-block:: console

   $ ros2 launch mocap4r2_gz_demos robot_groundtruth.launch.yaml system:=ros
   $ ros2 launch mocap4r2_gz_demos robot_groundtruth.launch.yaml system:=optitrack
   $ ros2 launch mocap4r2_gz_demos human_motion.launch.yaml

* **Robot ground truth**: a robot with a marker plate drives in circles; ``robot_gt``
  publishes ``base_link_gt``. With ``system:=optitrack`` Gazebo plays Motive and the real
  OptiTrack driver connects to it, as in the lab.
* **Human motion**: a walking mannequin streamed as a skeleton (and its head as a rigid
  body); ``skeleton_publisher`` publishes its segments as TF and its joint angles.

The guides walk through each one: :ref:`robot ground truth <gt-demo>` and
:ref:`human motion <human-demo>`.
