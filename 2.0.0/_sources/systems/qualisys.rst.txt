Qualisys (QTM)
##############

``mocap4r2_qualisys_driver`` uses the Qualisys C++ SDK (RT protocol 1.28, MIT license),
included in the package.

.. code-block:: console

   $ ros2 launch mocap4r2_qualisys_driver qualisys_driver.launch.yaml \
       params_file:=my_qualisys.yaml
   $ ros2 mocap4r2 start qualisys_driver

Enable real-time output in QTM (Project options > Real-time output).

Parameters
**********

.. list-table::
   :header-rows: 1

   * - Parameter
     - Default
     - Meaning
   * - ``server_address``
     - ``127.0.0.1``
     - QTM computer
   * - ``base_port``
     - 22222
     - RT protocol base port
   * - ``udp_port``
     - 0
     - 0: stream over TCP (robust everywhere); > 0: UDP on this port (lower latency)
   * - ``up_axis``
     - ``auto``
     - ``auto`` reads the up axis of the QTM calibration; or ``x``, ``-x``, ``y``,
       ``-y``, ``z``, ``-z``
   * - ``latency``
     - 0.0
     - seconds subtracted from the reception time (QTM does not report its latency)

Data
****

* 6DOF bodies are rigid bodies; untracked bodies (NaN in QTM) are published with
  ``tracking_valid: false``, never with NaN.
* Labeled markers keep their QTM label; markers whose label starts with a body name
  are also attached to that body.
* Skeletons are streamed in global coordinates with their segment hierarchy.
* All frames are streamed (``RateAllFrames``) to a dedicated thread.
