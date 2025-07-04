#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist


class JoyReader(Node):
    def __init__(self):
        super().__init__("joy_reader")

        # Create publisher
        self.cmd_vel_pub = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)

        # Create subscriber
        self.joy_sub = self.create_subscription(Joy, "/joy", self.joy_callback, 10)

        self.get_logger().info("Joystick node started")

    def joy_callback(self, joy_msg):
        # Example: assume axes[1] is forward/backward, axes[0] is left/right
        msg = Twist()
        msg.linear.x = joy_msg.axes[1]  # Forward/Backward
        msg.angular.z = joy_msg.axes[0]  # Left/Right

        self.cmd_vel_pub.publish(msg)
        self.get_logger().info(f"Published Twist: linear.x={msg.linear.x}, angular.z={msg.angular.z}")


def main(args=None):
    rclpy.init(args=args)
    node = JoyReader()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
