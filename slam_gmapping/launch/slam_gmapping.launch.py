from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
import os
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import PythonExpression


launch_rviz = LaunchConfiguration('launch_rviz')
launch_rviz_arg = DeclareLaunchArgument(
    'launch_rviz',
    default_value='false'
)

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')
    use_sim_time_arg = DeclareLaunchArgument(
        'use_sim_time',
        default_value='false'
        )
    
    return LaunchDescription([
        use_sim_time_arg,
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d',os.path.join(get_package_share_directory("slam_gmapping"),'config','slam_gmapping.rviz')],
            output='screen',
            condition=IfCondition(launch_rviz)
        ),
        Node(
            package='slam_gmapping',
            executable='slam_gmapping_node',
            name='slam_gmapping',
            output='screen',
            parameters=[
                {'use_sim_time': use_sim_time},
                os.path.join(get_package_share_directory("slam_gmapping"), 'config', 'slam_gmapping.yaml')
            ]
        ),
    ])