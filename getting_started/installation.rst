Installation
############

MOCAP4ROS2 2.0 supports every active ROS 2 distribution from a single code base.

.. list-table::
   :header-rows: 1

   * - Package
     - Humble
     - Jazzy
     - Kilted
     - Lyrical
     - Rolling
   * - Core, tools, simulated system
     - binary
     - binary
     - binary
     - binary
     - source
   * - OptiTrack, Vicon, Qualisys drivers
     - binary
     - binary
     - binary
     - binary
     - source
   * - Gazebo plugin
     - —
     - binary
     - binary
     - binary
     - source

Binary packages
***************

.. code-block:: console

   $ sudo apt install ros-$ROS_DISTRO-mocap4r2-control ros-$ROS_DISTRO-mocap4r2-tools \
       ros-$ROS_DISTRO-mocap4r2-sim-driver ros-$ROS_DISTRO-mocap4r2-marker-viz

and the driver of your system:

.. code-block:: console

   $ sudo apt install ros-$ROS_DISTRO-mocap4r2-optitrack-driver   # OptiTrack (Motive)
   $ sudo apt install ros-$ROS_DISTRO-mocap4r2-vicon-driver       # Vicon
   $ sudo apt install ros-$ROS_DISTRO-mocap4r2-qualisys-driver    # Qualisys (QTM)
   $ sudo apt install ros-$ROS_DISTRO-mocap4r2-gz-plugin          # Gazebo (Jazzy and newer)

Ground truth and human motion tools:

.. code-block:: console

   $ sudo apt install ros-$ROS_DISTRO-mocap4r2-robot-gt ros-$ROS_DISTRO-mocap4r2-gt-tools \
       ros-$ROS_DISTRO-mocap4r2-motion-tools

From source
***********

.. code-block:: console

   $ mkdir -p ~/mocap_ws/src && cd ~/mocap_ws/src
   $ git clone https://github.com/MOCAP4ROS2-Project/mocap4r2_msgs.git
   $ git clone https://github.com/MOCAP4ROS2-Project/mocap4r2.git
   $ git clone https://github.com/MOCAP4ROS2-Project/mocap4ros2_optitrack.git   # your system
   $ cd ~/mocap_ws
   $ rosdep install --from-paths src --ignore-src -y
   $ colcon build --symlink-install
   $ source install/setup.bash

The Vicon and Qualisys SDKs are included in their repositories (both are MIT licensed).
For OptiTrack, see :doc:`/systems/optitrack` to choose between the open NatNet
implementation (included) and the official NatNet SDK (installed separately).

Check the installation
**********************

.. code-block:: console

   $ ros2 mocap4r2 --help
   $ ros2 mocap4r2 doctor
