Terminal UI
###########

.. code-block:: console

   $ ros2 mocap4r2 tui

The top table lists every system: lifecycle state, measured and nominal rate, latency,
dropped frames, diagnostics status and session. The bottom table shows the rigid
bodies of the selected system: tracked or lost, tracking ratio, position and error,
and the counts of labeled, unlabeled and occluded markers.

.. list-table::
   :header-rows: 1

   * - Key
     - Action
   * - ↑ ↓
     - select a system
   * - ``s`` / ``x``
     - start / stop the selected system
   * - ``a`` / ``z``
     - start / stop all systems
   * - ``n``
     - set the session name used by the next start
   * - ``q``
     - quit

It works over SSH, in the robot or in the mocap room computer.

.. note::

   The TUI uses Textual, included in the package. On Humble (Ubuntu 22.04) the system
   Python packages are too old for it; install a newer Textual with
   ``pip install --user 'textual>=6'``. The rest of ``ros2 mocap4r2`` works with the
   system packages on every distribution.
