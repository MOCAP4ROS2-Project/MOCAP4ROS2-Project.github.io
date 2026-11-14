Vicon (Nexus, Tracker, Shogun)
##############################

``mocap4r2_vicon_driver`` uses the Vicon DataStream SDK 1.13, whose source code (MIT
license) is included in the package: nothing else needs to be installed, on x86_64 or
arm64.

.. code-block:: console

   $ ros2 launch mocap4r2_vicon_driver vicon_driver.launch.yaml params_file:=my_vicon.yaml
   $ ros2 mocap4r2 start vicon_driver

Enable the DataStream in the Vicon software (it listens on port 801 by default).

Parameters
**********

.. list-table::
   :header-rows: 1

   * - Parameter
     - Default
     - Meaning
   * - ``host_name``
     - ``192.168.10.1:801``
     - Vicon computer and DataStream port
   * - ``timeout``
     - 2.0
     - seconds to connect
   * - ``compensate_latency``
     - ``true``
     - stamp = reception time − total latency reported by the DataStream

Data
****

* Every **subject** is published as a rigid body: the pose of its root segment, its
  own markers (named ``subject:marker``) and ``tracking_valid: false`` when the root
  segment is occluded.
* Subjects with more than one segment are also published as **skeletons**, with the
  hierarchy of segments.
* Unlabeled markers are published with ``id: -1`` and no name.
* Frames are read in pre-fetch mode with a buffer of one frame (always the newest),
  and ``frame_number`` is Vicon's: gaps are dropped frames.
