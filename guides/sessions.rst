Capture sessions
################

A session is a trial: several systems started together, recorded, and stopped
together, with an id that every system reports.

.. code-block:: console

   $ ros2 mocap4r2 record --session walk01                  # all systems
   $ ros2 mocap4r2 record optitrack_driver --session walk02 --topics /odom /imu

``record`` starts the systems with the session id (and fails without recording if one
of them cannot start), records with rosbag2 every topic they announce plus ``/tf``,
``/tf_static``, ``/mocap4r2/systems``, ``/diagnostics`` and the extra ``--topics``,
and on Ctrl-C stops the bag and the systems. The bag directory gets a
``mocap4r2_session.yaml`` with the session, the start and end times and, for each
system, its type, frame, rate and topics.

Other devices in a session
**************************

Any device can join the sessions as an *auxiliary system*: it is started and stopped
with the mocap systems and its topics are recorded with them.

.. code-block:: yaml

   emg_recorder:
     ros__parameters:
       topics:
         - emg/raw:std_msgs/msg/Float64MultiArray
         - emg/status

.. code-block:: console

   $ ros2 launch mocap4r2_control auxiliar.launch.py params_file:=emg.yaml

From C++, derive from ``mocap4r2_control::MocapSystemNode`` to react to the start and
stop of each session (``on_control_start``/``on_control_stop`` receive the session id).
