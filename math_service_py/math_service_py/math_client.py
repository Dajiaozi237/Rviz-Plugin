import rclpy
from rclpy.node import Node
from math_service.srv import AddThreeFloats

class MathClient(Node):
    def __init__(self):
        super().__init__('math_client')
        self.cli = self.create_client(AddThreeFloats, 'math_operation')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
    
    def send_request(self, a, b, c):
        req = AddThreeFloats.Request()
        req.a = a
        req.b = b
        req.c = c
        future = self.cli.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        return future.result()

def main(args=None):
    rclpy.init(args=args)
    client = MathClient()
    
    try:
        a = float(input("Enter number A: "))
        b = float(input("Enter number B: "))
        c = float(input("Enter number C: "))
        
        response = client.send_request(a, b, c)

        print("Request sent. Check server logs for results.")
        
    except ValueError:
        print("Error: Please enter valid numbers")
    
    client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

