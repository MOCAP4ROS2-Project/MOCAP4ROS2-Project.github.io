Interfaces
##########

Package ``mocap4r2_interfaces``, repository :repo:`mocap4r2_interfaces` (they replace ``mocap4r2_msgs`` of 1.x; Open Robotics
reserves the ``mocap_*`` names, so every MOCAP4ROS2 package starts with ``mocap4r2_``).

Identifiers are stable: they come from the mocap system (never from the position in
an array), so the same marker or body keeps its id from frame to frame. Validity is
explicit: a body that is not tracked is published with ``tracking_valid: false`` and
its last pose, never with zeros or NaN.

Marker
******

.. code-block:: text

   # A single 3D marker measured by a motion capture system.
   # Positions are in the frame of the containing message header (Z-up, metres).
   
   int32 UNKNOWN_ID=-1
   
   # Stable identifier from the mocap SDK, or UNKNOWN_ID for unlabeled markers.
   int32 id
   # Label from the mocap software (e.g. "robot1:front_left"), empty if unlabeled.
   string name
   geometry_msgs/Point position
   # True when the marker is not seen in this frame; position then holds the last estimate.
   bool occluded
   # Reconstruction residual in metres, negative if unknown.
   float32 residual

Markers
*******

.. code-block:: text

   # All markers of one mocap frame.
   
   std_msgs/Header header
   # Frame number reported by the mocap system (shared with RigidBodies/Skeletons of the same frame).
   uint64 frame_number
   Marker[] markers

RigidBody
*********

.. code-block:: text

   # A tracked rigid body (asset, subject, 6DOF body) of a motion capture system.
   
   int32 UNKNOWN_ID=-1
   
   # Stable identifier from the mocap SDK, or UNKNOWN_ID.
   int32 id
   # Name given in the mocap software.
   string name
   # False when the body is not tracked in this frame; pose must not be used then.
   bool tracking_valid
   # Pose of the body frame in the header frame.
   geometry_msgs/Pose pose
   # Mean marker error in metres, negative if unknown.
   float32 mean_error
   # Markers of the body as measured in this frame, in the header frame.
   Marker[] markers

RigidBodies
***********

.. code-block:: text

   # All rigid bodies of one mocap frame.
   
   std_msgs/Header header
   # Frame number reported by the mocap system (shared with Markers/Skeletons of the same frame).
   uint64 frame_number
   RigidBody[] rigid_bodies

Segment
*******

.. code-block:: text

   # One segment (bone) of a skeleton.
   
   int32 NO_PARENT=-1
   
   int32 id
   string name
   # Id of the parent segment, or NO_PARENT for the root.
   int32 parent_id
   # False when the segment is not tracked in this frame.
   bool tracking_valid
   # Pose of the segment in the header frame.
   geometry_msgs/Pose pose

Skeleton
********

.. code-block:: text

   # An articulated body (human or robot skeleton) tracked by a motion capture system.
   
   int32 UNKNOWN_ID=-1
   
   int32 id
   string name
   bool tracking_valid
   Segment[] segments

Skeletons
*********

.. code-block:: text

   # All skeletons of one mocap frame.
   
   std_msgs/Header header
   # Frame number reported by the mocap system (shared with Markers/RigidBodies of the same frame).
   uint64 frame_number
   Skeleton[] skeletons

MocapSystemInfo
***************

.. code-block:: text

   # Announcement of a mocap system (driver) on /mocap4r2/systems (transient local).
   
   # Fully qualified node name of the driver, used as the system id.
   string system
   # Kind of system: "optitrack", "vicon", "qualisys", "gazebo", "sim", ...
   string type
   # Frame of the published data.
   string frame_id
   # Nominal frame rate in Hz, 0 if unknown.
   float64 frame_rate
   # Current lifecycle state of the driver.
   lifecycle_msgs/State state
   # Capture session of the last START request, empty if none.
   string session_id
   # Fully qualified topics published by the system and their types.
   string[] topics
   string[] topic_types

Control
*******

.. code-block:: text

   # Request to start or stop mocap systems, published on /mocap4r2/control.
   
   uint8 START=0
   uint8 STOP=1
   
   uint8 command
   # Unique id of this request, echoed in every ControlAck.
   string request_id
   # Capture session this request belongs to (e.g. a trial name), may be empty.
   string session_id
   # Fully qualified node name of the requester.
   string requester
   # Systems addressed (fully qualified node names); empty means all systems.
   string[] systems
   builtin_interfaces/Time stamp

ControlAck
**********

.. code-block:: text

   # Answer of a mocap system to a Control request, published on /mocap4r2/control_ack.
   
   string request_id
   string session_id
   # Fully qualified node name of the answering system.
   string system
   # Command being answered (Control.START / Control.STOP).
   uint8 command
   # True if the system reached the requested state.
   bool success
   # Reason when success is false.
   string message
   # Time at which the system reached the requested state.
   builtin_interfaces/Time stamp

TrajectoryError
***************

.. code-block:: text

   # Error of a robot pose estimate against the mocap ground truth.
   
   std_msgs/Header header
   # Associated pose pairs used.
   uint32 samples
   # Absolute trajectory error, metres (after alignment if aligned is true).
   float64 ate_rmse
   float64 ate_mean
   float64 ate_max
   # Relative pose error over the configured step: metres and radians.
   float64 rpe_trans_rmse
   float64 rpe_rot_rmse
   bool aligned
   # Alignment from the estimate frame to the ground-truth frame.
   geometry_msgs/Pose alignment

SetOrigin (service)
*******************

.. code-block:: text

   # Set the origin of a ground-truth frame.
   # If use_current is true, the current pose becomes the origin and origin is ignored.
   
   bool use_current
   geometry_msgs/Pose origin
   ---
   bool success
   string message
