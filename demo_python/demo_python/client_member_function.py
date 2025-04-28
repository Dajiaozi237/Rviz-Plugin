import sys
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
from demo_python.calculator import NumberCalculator 

class CalculatorClient(Node):
    def __init__(self):
        super().__init__('calculator_client')
        self.cli = self.create_client(AddTwoInts, 'calculate_numbers')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('服务未就绪，等待中...')
        self.local_calculator = NumberCalculator()  

    def calculate_three_numbers(self, a, b, c):

        sum_response = self.call_service(a, b)
        

        self.local_calculator.numbers = [a, b, c]
        product = self.local_calculator.product()
        
        self.get_logger().info(
            f"运算结果:\n"
            f"服务端加法: {a} + {b} = {sum_response}\n"
            f"客户端乘法: {a} × {b} × {c} = {product}"
        )

    def call_service(self, a, b):
        req = AddTwoInts.Request()
        req.a = int(a)
        req.b = int(b)
        future = self.cli.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        return future.result().sum

def main(args=None):
    rclpy.init(args=args)
    
    if len(sys.argv) != 4:
        print("使用方法: python3 client_node.py <a> <b> <c>")
        return

    client = CalculatorClient()
    client.calculate_three_numbers(
        float(sys.argv[1]), 
        float(sys.argv[2]), 
        float(sys.argv[3])
    )
    client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
