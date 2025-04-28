cmake_minimum_required(VERSION 3.8)
project(calculator_plugin)

# Default to C++17
set(CMAKE_CXX_STANDARD 17)

find_package(ament_cmake REQUIRED)
find_package(pluginlib REQUIRED)
find_package(Qt5 REQUIRED COMPONENTS Widgets)
find_package(rviz_common REQUIRED)

set(CMAKE_AUTOMOC ON)

add_library(${PROJECT_NAME} SHARED
  src/calculator_panel.cpp
)

ament_target_dependencies(${PROJECT_NAME}
  "pluginlib"
  "Qt5"
  "rviz_common"
)

pluginlib_export_plugin_description_file(rviz_common plugin_description.xml)

install(TARGETS ${PROJECT_NAME}
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
