Nokov (XINGYING)
################

``mocap4r2_nokov_driver`` is developed and maintained by `NOKOV
<https://github.com/NOKOV-MOCAP>`_ in its own repository,
`mocap4ros2_nokov <https://github.com/NOKOV-MOCAP/mocap4ros2_nokov/tree/v2.0>`_. It
derives from ``MocapSystemNode`` and publishes the MOCAP4ROS2 interfaces, so the CLI,
the terminal UI, ground truth and recording work with it as with any other system.

It uses the Nokov SDK, included in the repository as prebuilt libraries for x86_64,
aarch64 and armhf. It is not released as a binary package: build it from source.

.. raw:: html

   <figure class="mocap4r2-video">
     <video controls muted loop playsinline preload="metadata"
            src="../_static/videos/nokov_skeleton.mp4"></video>
     <figcaption>A skeleton from XINGYING in RViz, with the driver in the terminal UI.</figcaption>
   </figure>

   <figure class="mocap4r2-video">
     <video controls muted loop playsinline preload="metadata"
            src="../_static/videos/nokov_rigid_bodies.mp4"></video>
     <figcaption>Markers and rigid bodies from XINGYING.</figcaption>
   </figure>

   <p class="mocap4r2-video-credit">Videos: NOKOV.</p>

Installation
************

.. code-block:: console

   $ mkdir -p ~/mocap4r2_ws/src && cd ~/mocap4r2_ws/src
   $ git clone -b v2.0 https://github.com/NOKOV-MOCAP/mocap4ros2_nokov.git
   $ cd .. && rosdep install --from-paths src --ignore-src -r -y
   $ colcon build --symlink-install

With the MOCAP4ROS2 binary packages installed, ``rosdep`` brings
``mocap4r2_control`` and ``mocap4r2_interfaces``; ``dependency_repos.repos`` in the
repository builds them from source instead.

Usage
*****

.. code-block:: console

   $ ros2 launch mocap4r2_nokov_driver nokov_driver.launch.yaml \
       params_file:=my_nokov.yaml
   $ ros2 mocap4r2 start nokov_driver

The launch file also opens RViz with ``marker_viz`` (``rviz:=false`` to skip it) and
takes ``namespace`` and ``autostart``.

Parameters
**********

Besides the :doc:`parameters shared by all systems <index>`:

.. list-table::
   :header-rows: 1

   * - Parameter
     - Default
     - Meaning
   * - ``server_address``
     - ``192.168.50.177``
     - computer running XINGYING
   * - ``timeout``
     - 10.0
     - seconds to keep trying to reach XINGYING when the node is configured
   * - ``nominal_frame_rate``
     - 0.0
     - frame rate of the cameras in Hz, 0 when unknown
   * - ``up_axis``
     - ``z``
     - ``z`` keeps the data as it is; ``y`` rotates it into Z-up

Data
****

* Markers, rigid bodies and skeletons, in metres and Z-up, with the ids of XINGYING.
* Rigid bodies and skeleton segments that are not tracked are published with
  ``tracking_valid: false``.
* Stamps are compensated with the latency reported by the SDK.

Report problems with this driver in its repository:
https://github.com/NOKOV-MOCAP/mocap4ros2_nokov/issues
