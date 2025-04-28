#include <memory>
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

class SubNode : public rclcpp::Node {
public:
  SubNode() : Node("sub"), reset_count_(0) {
    subscription_ = this->create_subscription<std_msgs::msg::String>(
      "counter_info", 10, std::bind(&SubNode::topic_callback, this, std::placeholders::_1));
  }

private:
  void topic_callback(const std_msgs::msg::String::SharedPtr msg) {
    size_t comma_pos = msg->data.find(',');
    int current_count = std::stoi(msg->data.substr(0, comma_pos));
    std::string time_str = msg->data.substr(comma_pos + 1);
    
    RCLCPP_INFO(this->get_logger(), "Received - Time: %s, Count: %d", 
               time_str.c_str(), current_count);
    
    if (current_count == 0) {
      reset_count_++;
      RCLCPP_INFO(this->get_logger(), "嘿！我已经被清空%d次了！", reset_count_);
    }
  }
  
  rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
  int reset_count_;
};

int main(int argc, char * argv[]) {
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<SubNode>());
  rclcpp::shutdown();
  return 0;
}
