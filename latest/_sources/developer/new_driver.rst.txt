Writing a driver for a new system
#################################

A driver translates a mocap system into the MOCAP4ROS2 interfaces. Everything else —
lifecycle, start/stop, system announcement, diagnostics, stamps, frame numbers, TF —
comes from ``mocap4r2_control``, so every tool works with the new system from the
first frame.

.. code-block:: cpp

   #include "mocap4r2_control/frame_publisher.hpp"
   #include "mocap4r2_control/mocap_system_node.hpp"
   #include "mocap4r2_control/system_main.hpp"

   class MyDriver : public mocap4r2_control::MocapSystemNode
   {
   public:
     explicit MyDriver(const rclcpp::NodeOptions & options = rclcpp::NodeOptions())
     : MocapSystemNode("my_driver", "my_system", options)
     {
       declare_parameter<std::string>("server", "192.168.1.5");
       mocap4r2_control::declare_frame_publisher_parameters(*this);
     }

     ~MyDriver() override {stop();}  // stop SDK threads before the node goes away

   protected:
     CallbackReturn on_system_configure() override
     {
       sdk_.connect(get_parameter("server").as_string());  // throw on failure
       publisher_ = std::make_unique<mocap4r2_control::FramePublisher>(*this);
       return CallbackReturn::SUCCESS;
     }
     CallbackReturn on_system_activate() override
     {
       sdk_.on_frame([this](const SdkFrame & f) {frame(f);});  // SDK thread
       return CallbackReturn::SUCCESS;
     }
     CallbackReturn on_system_deactivate() override {stop(); return CallbackReturn::SUCCESS;}
     CallbackReturn on_system_cleanup() override
     {
       sdk_.disconnect();
       publisher_.reset();
       return CallbackReturn::SUCCESS;
     }
     double nominal_frame_rate() const override {return sdk_.rate();}

   private:
     void frame(const SdkFrame & f)
     {
       mocap4r2_control::MocapFrame out;
       out.frame_number = f.number;                     // the system's own number
       out.capture_time = now() - rclcpp::Duration::from_seconds(f.latency);
       // fill out.markers, out.rigid_bodies, out.skeletons: metres, Z-up,
       // stable ids, tracking_valid = false for untracked bodies
       publisher_->publish(std::move(out));             // thread safe, drops if inactive
     }
     void stop() {sdk_.on_frame(nullptr);}

     MySdk sdk_;
     std::unique_ptr<mocap4r2_control::FramePublisher> publisher_;
   };

   int main(int argc, char ** argv)
   {
     return mocap4r2_control::system_main<MyDriver>(argc, argv);
   }

Rules
*****

* Convert to **metres** and **Z-up** in the driver; never leave axis fixes to consumers.
* Ids must be **stable** across frames (from the SDK or from names); never use the
  position in an array.
* Never publish NaN or zero poses for untracked bodies: set ``tracking_valid: false``.
* Read the SDK in its own thread; the base class gives you ``is_active()`` and the
  ``FramePublisher`` is safe to call from any thread.
* Stop every SDK thread in ``on_system_deactivate``/``on_system_cleanup`` and in the
  destructor.
* Write the SDK-independent part (frame conversion) as pure functions and test them;
  the existing drivers test their integration against fake servers or fake sources.

The OptiTrack, Vicon and Qualisys drivers are complete examples of this structure.
