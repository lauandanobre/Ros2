import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/robofei/Documents/Ros2_basic/lau_ws/install/my_robot_controller'
