from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'math_rviz_plugin_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['plugin_description.xml']),
    ],
    install_requires=['setuptools', 'rviz2', 'python_qt_binding'],
    zip_safe=False,
    maintainer='dajiaozi',
    maintainer_email='dajiaozi@todo.todo',
    description='A RViz2 panel for math operations',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
        'rviz2.plugin': [
            'MathPanel = math_rviz_plugin_py.math_panel:MathPanel',
        ],
    },
)
