import rclpy
from rclpy.node import Node
from math_service.srv import AddThreeFloats

class MathServer(Node):
    def __init__(self):
        super().__init__('math_server')
        self.srv = self.create_service(
            AddThreeFloats,
            'math_operation',
            self.math_callback)
        self.get_logger().info("Service started and ready...")

    def math_callback(self, request, response):
        try:

            self.get_logger().info(
                f"Raw request - a: {type(request.a)}={request.a}, "
                f"b: {type(request.b)}={request.b}, "
                f"c: {type(request.c)}={request.c}"
            )


            a = float(request.a)
            b = float(request.b)
            c = float(request.c)

            response.sum_result = a + b + c
            response.product_result = a * b * c


            self.get_logger().info(
                f"Calculated - sum: {response.sum_result}, "
                f"product: {response.product_result}"
            )

            return response 

        except Exception as e:
            self.get_logger().error(f"Calculation failed: {str(e)}")
            raise

def main():
    rclpy.init()
    server = MathServer()
    try:
        rclpy.spin(server)
    except KeyboardInterrupt:
        server.get_logger().info("Server stopped manually")
    finally:
        server.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
