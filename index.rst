:layout: landing

MOCAP4ROS2
##########

.. container:: mocap4r2-hero

   .. image:: /images/mocap4r2_logo_light.png
      :alt: MOCAP4ROS2
      :class: light-only

   .. image:: /images/mocap4r2_logo_dark.png
      :alt: MOCAP4ROS2
      :class: dark-only

.. rst-class:: lead

   Motion capture for ROS 2: one interface for OptiTrack, Vicon, Qualisys and Gazebo,
   and tools that work with all of them — ground truth for robots, human motion
   analysis, recording and monitoring.

.. container:: buttons

   `Get started <getting_started/index.html>`_
   `GitHub <https://github.com/MOCAP4ROS2-Project>`_

.. grid:: 1 1 2 3
   :gutter: 2
   :padding: 0
   :class-row: surface

   .. grid-item-card:: :octicon:`plug` Drivers for real systems
      :link: systems/index
      :link-type: doc

      OptiTrack (official NatNet SDK or open implementation), Vicon DataStream 1.13,
      Qualisys QTM, plus a simulated system and a Gazebo plugin.

   .. grid-item-card:: :octicon:`git-branch` One interface
      :link: concepts/architecture
      :link-type: doc

      Markers, rigid bodies and skeletons with tracking validity, stable ids and one
      frame convention, whatever the system.

   .. grid-item-card:: :octicon:`location` Robot ground truth
      :link: guides/robot_groundtruth
      :link-type: doc

      A TF tree parallel to your robot's, body calibration, map alignment and online
      ATE/RPE with export for evo.

   .. grid-item-card:: :octicon:`person` Human motion
      :link: guides/human_motion
      :link-type: doc

      Skeletons as TF and joint angles, zero-phase filtering, gap filling and C3D
      export for biomechanics software.

   .. grid-item-card:: :octicon:`terminal` CLI and terminal UI
      :link: tools/index
      :link-type: doc

      ``ros2 mocap4r2`` lists, starts, stops, records and diagnoses every system;
      the TUI shows rates, latency and tracking live.

   .. grid-item-card:: :octicon:`code` Add your system
      :link: developer/new_driver
      :link-type: doc

      A driver only translates its system into the MOCAP4ROS2 interfaces: every
      tool works with it from the first frame.

.. toctree::
   :hidden:

   getting_started/index
   concepts/index
   systems/index
   guides/index
   tools/index
   developer/index
   about/index
