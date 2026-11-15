Architecture
############

MOCAP4ROS2 separates **drivers** from **tools**. A driver only translates its system
into the MOCAP4ROS2 interfaces; every tool works on those interfaces and never needs
to know which system produced the data.

.. image:: /images/architecture_light.png
   :alt: MOCAP4ROS2 architecture: drivers publish mocap4r2_interfaces, tools consume them
   :class: light-only

.. image:: /images/architecture_dark.png
   :alt: MOCAP4ROS2 architecture: drivers publish mocap4r2_interfaces, tools consume them
   :class: dark-only

Systems
*******

Every system is a lifecycle node derived from ``mocap4r2_control::MocapSystemNode``:

* **configure** connects to the mocap software (Motive, Vicon, QTM) and reads the
  names of the assets;
* **activate** starts streaming (frames are read in a dedicated thread, never in the
  ROS executor);
* **deactivate** stops streaming; **cleanup** disconnects.

Each system publishes, in its namespace:

.. list-table::
   :header-rows: 1

   * - Topic
     - Type
     - Content
   * - ``markers``
     - ``mocap4r2_interfaces/Markers``
     - every marker of a frame, labeled or not, with occlusion flags
   * - ``rigid_bodies``
     - ``mocap4r2_interfaces/RigidBodies``
     - pose and tracking validity of each rigid body, with its markers
   * - ``skeletons``
     - ``mocap4r2_interfaces/Skeletons``
     - segments of articulated bodies (humans, animals, robots)
   * - ``/tf`` (optional)
     - ``tf2_msgs/TFMessage``
     - ``frame_id -> <tf_prefix><body>`` for every tracked body
   * - ``/diagnostics``
     - ``diagnostic_msgs/DiagnosticArray``
     - rate, latency, dropped frames and tracking ratio per body

The three data topics of a frame share the same stamp (capture time, compensated
with the latency reported by the system) and the same ``frame_number`` (the one of
the mocap system, so gaps are dropped frames).

Control plane
*************

Systems are discovered and controlled through three well known topics:

``/mocap4r2/systems`` (``MocapSystemInfo``, transient local)
   Every system announces its type, frame, nominal rate, lifecycle state, current
   session and topics at each transition. Late joiners get the last announcement.

``/mocap4r2/control`` (``Control``)
   START or STOP requests for some systems (or all), with a request id and a
   capture session id.

``/mocap4r2/control_ack`` (``ControlAck``)
   The answer of each system: whether it really reached the requested state and why
   not otherwise.

This lets several systems start together for a capture session (for example a mocap
system, an EMG recorder registered as an ``AuxiliarSystem`` and a force plate), and
lets the CLI, the TUI or your application know what happened.
