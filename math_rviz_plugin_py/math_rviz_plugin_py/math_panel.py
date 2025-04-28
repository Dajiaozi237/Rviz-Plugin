from python_qt_binding.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
from rclpy.node import Node
from math_service.srv import AddThreeFloats
import rclpy
from rviz_common.panel import Panel

class MathPanel(Panel):
    def __init__(self, parent=None):
        super(MathPanel, self).__init__(parent)
        self.setObjectName('MathPanel')
        

        self.widget = QWidget()
        self.layout = QVBoxLayout()
        
        self.label_a = QLabel('Number A:')
        self.input_a = QLineEdit()
        
        self.label_b = QLabel('Number B:')
        self.input_b = QLineEdit()
        
        self.label_c = QLabel('Number C:')
        self.input_c = QLineEdit()
        
        self.calculate_btn = QPushButton('Calculate')
        self.calculate_btn.clicked.connect(self.calculate)
        
        self.result_label = QLabel('Results will appear here')
        
        self.layout.addWidget(self.label_a)
        self.layout.addWidget(self.input_a)
        self.layout.addWidget(self.label_b)
        self.layout.addWidget(self.input_b)
        self.layout.addWidget(self.label_c)
        self.layout.addWidget(self.input_c)
        self.layout.addWidget(self.calculate_btn)
        self.layout.addWidget(self.result_label)
        
        self.widget.setLayout(self.layout)
        self.set_widget(self.widget)
        

        if not rclpy.ok():
            rclpy.init()
        
        self.node = Node('math_rviz_plugin_node')
        self.client = self.node.create_client(AddThreeFloats, 'math_operation')
        

        self.timer = self.node.create_timer(1.0, self.check_service_availability)
        self.service_available = False
        
    def check_service_availability(self):
        self.service_available = self.client.wait_for_service(timeout_sec=0.1)
        self.calculate_btn.setEnabled(self.service_available)
        
    def calculate(self):
        if not self.service_available:
            self.result_label.setText("Service not available")
            return
            
        try:
            a = float(self.input_a.text())
            b = float(self.input_b.text())
            c = float(self.input_c.text())
            
            req = AddThreeFloats.Request()
            req.a = a
            req.b = b
            req.c = c
            
            future = self.client.call_async(req)
            future.add_done_callback(self.handle_service_response)
            
        except ValueError:
            self.result_label.setText("Please enter valid numbers")
    
    def handle_service_response(self, future):
        try:
            response = future.result()
            if response is not None:
                self.result_label.setText(
                    f"Sum: {response.sum_result}\nProduct: {response.product_result}")
            else:
                self.result_label.setText("Service call failed")
        except Exception as e:
            self.result_label.setText(f"Error: {str(e)}")
            
    def shutdown_plugin(self):

        if hasattr(self, 'timer'):
            self.node.destroy_timer(self.timer)
        self.node.destroy_node()
        super(MathPanel, self).shutdown_plugin()
