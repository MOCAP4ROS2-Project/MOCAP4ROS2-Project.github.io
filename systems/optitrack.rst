OptiTrack (Motive)
##################

``mocap4r2_optitrack_driver`` connects to Motive through NatNet, the streaming protocol
of OptiTrack.

.. code-block:: console

   $ ros2 launch mocap4r2_optitrack_driver optitrack_driver.launch.py \
       params_file:=my_optitrack.yaml
   $ ros2 mocap4r2 start optitrack_driver

Motive settings
***************

In Motive, open **Edit > Settings > Streaming** (or the Data Streaming pane):

* **Broadcast Frame Data**: on.
* **Local Interface**: the IP of the Motive computer on the network shared with ROS
  (not *loopback*, unless ROS runs on the same computer). This is ``server_address``.
* **Transmission Type**: *Multicast* (default) or *Unicast*. With ``connection_type:
  auto`` the driver uses what Motive announces.
* **Up Axis**: *Y* (default) or *Z*. Set the same in ``up_axis``; the data is always
  published Z-up.
* **Rigid Bodies**, **Labeled Markers**, **Unlabeled Markers**, **Skeletons**: enable
  what you need. **Skeleton Coordinates** must match ``skeleton_coordinates``.
* Command port 1510 and data port 1511 (defaults) must be open in the firewall of
  both computers.

Parameters
**********

.. list-table::
   :header-rows: 1

   * - Parameter
     - Default
     - Meaning
   * - ``backend``
     - ``auto``
     - ``sdk`` (official NatNet SDK), ``open`` (open implementation) or ``auto`` (SDK if
       this build has it, otherwise open). See below.
   * - ``server_address``
     - ``127.0.0.1``
     - Motive computer (its *Local Interface*)
   * - ``local_address``
     - ``0.0.0.0``
     - interface of this computer towards Motive (needed for multicast on hosts with
       several networks)
   * - ``connection_type``
     - ``auto``
     - ``auto``, ``multicast`` or ``unicast``
   * - ``multicast_address``
     - (from Motive)
     - multicast group, ``239.255.42.99`` by default
   * - ``server_command_port`` / ``server_data_port``
     - 1510 / (from Motive)
     - NatNet ports
   * - ``up_axis``
     - ``y``
     - up axis of the Motive stream: ``y`` or ``z``
   * - ``skeleton_coordinates``
     - ``global``
     - ``global`` or ``local`` (as in Motive)
   * - ``compensate_latency``
     - ``true``
     - stamp = reception time − latency measured by Motive (camera mid-exposure to
       transmission)
   * - ``timeout``
     - 2.0
     - seconds to wait for Motive answers

NatNet: official SDK or open implementation
*******************************************

The driver can talk NatNet in two ways, called *backends*. Both produce exactly the
same ROS messages: the CI runs the same integration tests with both, and a test
checks that they publish identical messages for the same stream.

**Official NatNet SDK** (``backend: sdk``)
   OptiTrack's own client library (``libNatNet.so``). It is governed by the OptiTrack
   Plugins EULA, so it cannot be redistributed in the ROS binary packages: it is
   installed separately and the driver is built from source with it.

**Open implementation** (``backend: open``)
   An implementation of the NatNet protocol (bitstream 3.0 to 4.5, newer versions read
   skipping unknown data) written for MOCAP4ROS2 and released under Apache 2.0. It is
   what the ROS binary packages contain, and it works on every architecture (x86_64,
   arm64). It has been checked against the official client: the official NatNet 4.4
   client decodes everything the open encoder produces, in unicast and multicast and
   for bitstreams 3.1, 4.0, 4.1 and 4.4.

Which one should I use?
=======================

* Installed from binaries (``apt``): you are using the open implementation; nothing
  else is needed.
* You want OptiTrack's library (for example, for support from OptiTrack, or new
  features of a recent Motive before they reach the open implementation): install
  the SDK and build the driver from source, as below.

Install the official SDK
========================

1. Read the `OptiTrack Plugins EULA <https://www.optitrack.com/about/legal/eula.html>`_.
2. Download the SDK for your architecture (x86_64 or arm64) into
   ``~/.local/share/natnet_sdk``:

   .. code-block:: console

      $ ros2 run mocap4r2_optitrack_driver install_natnet_sdk.sh --accept-eula

   or, from a source workspace,
   ``src/mocap4ros2_optitrack/mocap4r2_optitrack_driver/scripts/install_natnet_sdk.sh``.
   Use ``--dir`` (or the environment variable ``NATNET_SDK_DIR``) for another location.
3. Build the driver from source (CMake looks for the SDK in ``NATNET_SDK_DIR`` or
   ``~/.local/share/natnet_sdk``):

   .. code-block:: console

      $ colcon build --packages-select mocap4r2_optitrack_driver --cmake-clean-cache

   The build log says ``NatNet SDK found: ... (backends: sdk, open)``.

Which backend am I using?
=========================

The driver says it when it connects:

.. code-block:: text

   [optitrack_driver]: connected to Motive 3.1.0.0 (NatNet 4.4.0.0, multicast, sdk backend)

``backend: sdk`` on a build without the SDK fails to configure with an explicit
message (``run install_natnet_sdk.sh and rebuild, or use backend 'open'``).

Test without Motive
*******************

``natnet_simulator`` is a stand-in for Motive that streams moving rigid bodies with
any NatNet version:

.. code-block:: console

   $ ros2 run mocap4r2_optitrack_driver natnet_simulator --bodies 2 --rate 120
   $ ros2 launch mocap4r2_optitrack_driver optitrack_driver.launch.py autostart:=activate

(``--multicast``, ``--version 4.1``, ``--up-axis z``... see ``--help``). The Gazebo
plugin can also play Motive: :doc:`gazebo`.

Troubleshooting
***************

``configure failed: no answer from NatNet server``
   ``server_address`` is not Motive's *Local Interface*, the firewall blocks port 1510,
   or streaming is off. ``ros2 mocap4r2 doctor`` shows the route to the server.

Connected, but no frames (multicast)
   The multicast group does not reach this computer: set ``local_address`` to the IP of
   the interface towards Motive, check the switch (IGMP snooping) or use
   ``connection_type: unicast`` (and *Unicast* in Motive).

Bodies upside down or rotated 90°
   ``up_axis`` does not match the *Up Axis* of Motive.

Bodies named by numbers
   The asset list changed and could not be reloaded; restart the driver (normally it
   reloads the names when Motive reports a change).
