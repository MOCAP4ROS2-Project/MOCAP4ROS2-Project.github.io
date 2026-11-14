Frames and conventions
######################

Units and axes
**************

All data is in **metres** and in a **Z-up, right-handed** frame (`REP-103
<https://www.ros.org/reps/rep-0103.html>`_), whatever the convention of the mocap
software:

* OptiTrack Motive streams Y-up by default: set ``up_axis: y`` (the default) and the
  driver rotates positions and orientations to Z-up. If Motive streams Z-up, set
  ``up_axis: z``.
* Qualisys QTM uses the up axis of its calibration; the driver reads it
  (``up_axis: auto``) and converts any of ±X, ±Y, ±Z.
* Vicon is already Z-up; the driver converts millimetres to metres.

The frame of the data is the ``frame_id`` parameter of each driver (``mocap`` by
default): the world frame of the mocap room.

Ground truth of a robot
***********************

A robot already has a TF tree (``map -> odom -> base_link``, `REP-105
<https://www.ros.org/reps/rep-0105.html>`_). The ground truth must **never** publish
into that tree: the localization of the robot owns it. ``mocap4r2_robot_gt`` publishes
a parallel tree:

.. code-block:: text

   mocap ──► gt_origin ──► base_link_gt          (ground truth, robot_gt)

   map ────► odom ───────► base_link             (the robot, untouched)

* ``mocap -> gt_origin`` is the origin of the ground truth: identity until you call
  ``~/set_origin`` (for example, to start the ground truth at the robot's start pose);
* ``gt_origin -> base_link_gt`` is the robot pose measured by the mocap system,
  already corrected by the position of the marker body on the robot.

To compare the robot localization with the ground truth in one tree, calibrate
``map -> mocap`` once with the ``frame_aligner`` (see
:doc:`/guides/robot_groundtruth`):

.. code-block:: text

   map ──► mocap ──► gt_origin ──► base_link_gt
    └────► odom ───► base_link

Now ``map -> base_link`` (estimate) and ``map -> base_link_gt`` (ground truth) can be
compared directly, in RViz or with ``gt_evaluator``.

Marker body on the robot
************************

The rigid body defined in the mocap software is rarely centred on ``base_link``.
``robot_gt`` needs the pose of the robot frame in the body frame:

* from the parameter ``body_to_robot: [x, y, z, roll, pitch, yaw]``, measured or
  calibrated with ``body_calibrator``; or
* from TF, if the robot URDF has a frame for the marker body (``body_frame``).
