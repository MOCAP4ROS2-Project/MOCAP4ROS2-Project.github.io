Human motion
############

Skeletons
*********

Skeletons of OptiTrack, Vicon (subjects with several segments) and Qualisys are
published on ``skeletons`` with the same structure: segments with ids, names, parent
and global pose. ``mocap4r2_marker_viz`` draws them, and ``skeleton_publisher`` turns
them into TF (``<skeleton>/<segment>``, to use RViz or ``tf2`` tools) and joint
angles:

.. code-block:: console

   $ ros2 run mocap4r2_motion_tools skeleton_publisher --ros-args \
       -r skeletons:=/skeletons

``~/joint_states`` (``sensor_msgs/JointState``) has three angles per segment with a
parent, ``<skeleton>/<segment>_{x,y,z}``: the Cardan XYZ angles (mobile axes) of the
segment relative to its parent. Map them to your anatomical convention (e.g. ISB) with
the segment axes defined in the mocap software.

Capture sessions
****************

See :doc:`sessions` to record a trial with every system started at once and its
metadata.

Export for biomechanics software
********************************

.. code-block:: console

   $ ros2 mocap4r2 export walk01 --format c3d --max-gap 10 --lowpass 6

* ``c3d``: labeled markers in millimetres, readable by Visual3D, OpenSim, Mokka and
  ezc3d; missing samples are flagged as invalid.
* ``csv``: one column per marker coordinate, and one file per rigid body.
* ``tum``: rigid body trajectories for evo.

``--max-gap N`` fills gaps of up to N frames by linear interpolation; ``--lowpass F``
applies a zero-phase second order Butterworth filter (forward and backward, the usual
choice for marker data; 6 Hz is common for gait).

.. _human-demo:

Try it in simulation
********************

``mocap4r2_gz_demos`` (Jazzy and newer) streams a walking mannequin from Gazebo as the
skeleton ``walker`` (and its head as the rigid body ``head``), with
``skeleton_publisher`` already running:

.. code-block:: console

   $ ros2 launch mocap4r2_gz_demos human_motion.launch.yaml

RViz shows the skeleton and the TF of its segments (``walker/<segment>``). In another
terminal:

.. code-block:: console

   $ ros2 mocap4r2 tui                                   # rate, latency and tracking
   $ ros2 topic echo /skeleton_publisher/joint_states    # joint angles

And the whole biomechanics chain, from recording to a C3D file:

.. code-block:: console

   $ ros2 mocap4r2 record --session walk01               # Ctrl-C to finish
   $ ros2 mocap4r2 export walk01 --format c3d --max-gap 10 --lowpass 6
