
import rclpy
from rclpy.node import Node

class MyFirstNode(Node):

    def __init__(self) -> None:
        super().__init__("my_first_node")
        self.get_logger().info("Hello World!!")


def main(args = None):
    rclpy.init(args=args)
    # nó
    node = MyFirstNode()
    rclpy.spin(node) # manter em execução no terminal
    rclpy.shutdown()


if __name__ == "__main__":
    main()
