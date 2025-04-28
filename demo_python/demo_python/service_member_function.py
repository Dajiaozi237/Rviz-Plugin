import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
from demo_python.calculator import NumberCalculator  

class CalculatorService(Node):
    def __init__(self):
        super().__init__('calculator_service')
        self.srv = self.create_service(
            AddTwoInts, 
            'calculate_numbers', 
            self.calculate_callback
        )
        self.calculator = NumberCalculator()  
        
    def calculate_callback(self, request, response):
        
        self.calculator.numbers = [request.a, request.b]
        
        
        response.sum = int(self.calculator.sum())  
        
        self.get_logger().info(
            f'计算: {request.a} + {request.b} = {response.sum}'
        )
        return response

def main(args=None):
    rclpy.init(args=args)
    node = CalculatorService()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
