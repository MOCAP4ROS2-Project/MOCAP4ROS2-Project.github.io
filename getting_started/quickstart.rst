Quickstart: a mocap system in two minutes
#########################################

No hardware is needed: ``mocap4r2_sim_driver`` is a mocap system that streams two
moving rigid bodies with markers, noise, occlusions and latency, exactly as a real
driver does.

1. Start the simulated system (it configures and waits for a start request):

   .. code-block:: console

      $ ros2 launch mocap4r2_sim_driver sim_driver.launch.yaml

2. In another terminal, list the systems and start it:

   .. code-block:: console

      $ ros2 mocap4r2 list
      SYSTEM       TYPE  STATE     FRAME  RATE    SESSION
      /sim_driver  sim   inactive  mocap  120 Hz  -
      $ ros2 mocap4r2 start sim_driver --session trial1
      /sim_driver: started

3. Watch it:

   .. code-block:: console

      $ ros2 mocap4r2 hz
      $ ros2 mocap4r2 bodies sim_driver
      $ ros2 launch mocap4r2_marker_viz marker_viz.launch.yaml

4. Or open the terminal UI, where ``s``/``x`` start and stop the selected system:

   .. code-block:: console

      $ ros2 mocap4r2 tui

5. Record a session and export it:

   .. code-block:: console

      $ ros2 mocap4r2 record --session walk01        # Ctrl-C to finish
      $ ros2 mocap4r2 export walk01 --format c3d

Every command works the same with a real system: replace the simulated driver by
the driver of :doc:`your system </systems/index>`.

The real OptiTrack driver, without Motive
*****************************************

``natnet_simulator`` plays Motive on this computer; the OptiTrack driver connects to
it exactly as it would to Motive:

.. code-block:: console

   $ ros2 run mocap4r2_optitrack_driver natnet_simulator
   $ ros2 launch mocap4r2_optitrack_driver optitrack_driver.launch.yaml \
       params_file:=$(ros2 pkg prefix mocap4r2_optitrack_driver)/share/mocap4r2_optitrack_driver/config/optitrack_simulator.yaml
   $ ros2 mocap4r2 tui

In the TUI the status box shows the driver connected to *FakeMotive*; the
*Start* button activates it and the bodies appear below. Stop
``natnet_simulator`` while the driver is active and the link turns to *connected,
no data*.
