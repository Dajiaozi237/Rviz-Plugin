#include <chrono>
#include <memory>
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

using namespace std::chrono_literals;

struct CounterInfo {
  int count;
  std::string time_str;
};

class PubNode : public rclcpp::Node {
public:
  PubNode() : Node("pub"), count_(0) {
    publisher_ = this->create_publisher<std_msgs::msg::String>("counter_info", 10);
    timer_ = this->create_wall_timer(
      1000ms, std::bind(&PubNode::timer_callback, this));
  }

private:
  void timer_callback() {
    auto now = std::chrono::system_clock::now();
    auto now_time = std::chrono::system_clock::to_time_t(now);
    std::string time_str = std::ctime(&now_time);
    time_str.erase(time_str.find_last_not_of("\n") + 1);  // Remove newline
    
    count_ = (count_ + 1) % 100;  // Reset to 0 when reaches 100
    
    auto message = std_msgs::msg::String();
    message.data = std::to_string(count_) + "," + time_str;
    publisher_->publish(message);
    
    RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
  }
  
  rclcpp::TimerBase::SharedPtr timer_;
  rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
  int count_;
};

int main(int argc, char * argv[]) {
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<PubNode>());
  rclcpp::shutdown();
  return 0;
}
