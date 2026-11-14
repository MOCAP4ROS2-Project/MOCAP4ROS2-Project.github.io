Ground truth for robots
#######################

This guide gives a robot a ground truth from the mocap system and measures the error
of its localization. Read :doc:`/concepts/frames` first: the ground truth lives in a
TF tree parallel to the robot's.

1. Define the rigid body
************************

Put at least three markers on the robot (asymmetric, not on a line, visible from
above) and create a rigid body in the mocap software, for example ``robot``. Check it:

.. code-block:: console

   $ ros2 mocap4r2 bodies optitrack_driver

2. Run robot_gt
***************

.. code-block:: yaml

   robot_gt:
     ros__parameters:
       rigid_body: robot
       robot_frame: base_link        # gt_frame defaults to base_link_gt
       body_to_robot: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]   # calibrated in step 3

.. code-block:: console

   $ ros2 launch mocap4r2_robot_gt robot_gt.launch.yaml params_file:=robot_gt.yaml

It publishes TF ``mocap -> gt_origin -> base_link_gt``, ``~/pose`` and ``~/odom``
(``nav_msgs/Odometry`` with velocities in the robot frame, filtered with
``velocity_alpha``). Untracked or missing bodies produce nothing: a ground truth is
never extrapolated.

3. Calibrate the body on the robot
**********************************

``body_calibrator`` finds ``body_to_robot``: the base of the robot is the centre of the
circle the body traces when the robot turns in place, and the direction of a straight
drive gives the yaw between the body and the robot.

.. code-block:: console

   $ ros2 run mocap4r2_gt_tools body_calibrator --ros-args -p rigid_body:=robot \
       -r rigid_bodies:=/rigid_bodies -p base_height:=0.0
   $ ros2 service call /body_calibrator/reset std_srvs/srv/Trigger
   # turn the robot in place at least 90 degrees
   $ ros2 service call /body_calibrator/turn_done std_srvs/srv/Trigger
   # drive straight forward at least 0.3 m
   $ ros2 service call /body_calibrator/compute std_srvs/srv/Trigger

It answers (and saves to ``body_to_robot.yaml``) the value for ``robot_gt``.
``base_height`` is the height of the robot frame origin over the mocap floor (0 for
``base_footprint``).

4. Align the map with the mocap room
************************************

To compare the localization (``map -> base_link``) with the ground truth, find
``map -> mocap`` while the robot drives around with its localization running:

.. code-block:: console

   $ ros2 run mocap4r2_gt_tools frame_aligner
   # drive around the room
   $ ros2 service call /frame_aligner/compute std_srvs/srv/Trigger

It publishes ``map -> mocap`` as a static transform and saves it
(``map_to_mocap.yaml``) to publish it in later runs with
``static_transform_publisher``. ``planar: true`` (default) fits a yaw and a translation,
which suits robots on a floor.

5. Measure the error
********************

.. code-block:: console

   $ ros2 launch mocap4r2_gt_tools gt_evaluation.launch.yaml output_dir:=run1

``gt_evaluator`` samples both trajectories at the same instants (TF interpolation)
and publishes on ``~/error`` (``TrajectoryError``) the ATE (after alignment, unless
``align: false``) and the RPE over ``rpe_delta`` samples. When it ends it writes
``run1/estimate.tum`` and ``run1/groundtruth.tum``, ready for
`evo <https://github.com/MichaelGrupp/evo>`_:

.. code-block:: console

   $ evo_ape tum run1/groundtruth.tum run1/estimate.tum -a --plot

Time synchronization
********************

Mocap stamps come from the computer running the driver. If the robot has another
clock, synchronize both (chrony/PTP). ``ros2 mocap4r2 doctor`` warns when the stamps of
a system are far from the ROS clock. ``mocap4r2_gt_tools.trajectory.time_offset``
estimates the offset between two signals (for example the yaw rate of the ground
truth and of the robot IMU) by cross-correlation.
