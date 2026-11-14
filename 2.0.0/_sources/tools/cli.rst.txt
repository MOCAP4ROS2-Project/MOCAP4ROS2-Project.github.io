Command line: ros2 mocap4r2
###########################

``mocap4r2_tools`` adds the ``mocap4r2`` command to ``ros2``. Systems can be named by
their fully qualified node name (``/lab/optitrack_driver``) or by their plain name if
it is unique (``optitrack_driver``).

.. list-table::
   :header-rows: 1

   * - Command
     - What it does
   * - ``list [--all]``
     - systems with type, lifecycle state, frame, nominal rate and session
   * - ``info SYSTEM``
     - details of a system and its topics with types
   * - ``start [SYSTEMS] [--session S]``
     - start systems (all if none is given); exits with an error if one does not start,
       printing why
   * - ``stop [SYSTEMS]``
     - stop systems
   * - ``bodies SYSTEM``
     - table of the rigid bodies of the last frame
   * - ``hz [--once]``
     - measured rate against nominal, latency, dropped frames and tracking ratio of each
       body
   * - ``record [SYSTEMS] [--session S] [-o DIR] [--topics ...]``
     - a capture session recorded with rosbag2 (see :doc:`/guides/sessions`)
   * - ``export BAG -f csv|tum|c3d [--lowpass HZ] [--max-gap N]``
     - export a recorded session
   * - ``doctor``
     - check the setup (see below)
   * - ``tui``
     - the terminal UI (:doc:`tui`)

doctor
******

``ros2 mocap4r2 doctor`` observes the systems for a few seconds and checks:

* the ROS setup (RMW, domain, discovery limited to localhost);
* that systems are announced, and their state (an unconfigured driver usually means
  the mocap software did not answer);
* frames flowing at the nominal rate, dropped frames, tracking ratio of each body;
* stamps close to the ROS clock (clock synchronization, ``use_sim_time`` mismatch);
* the route and interface to the server of each driver, and the MULTICAST flag of
  that interface.

It prints one line per check (``✔``, ``!``, ``✘``) and exits with an error if one fails.
