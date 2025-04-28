from setuptools import find_packages, setup

package_name = 'math_service_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/srv', ['srv/MathOperation.srv']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dajiaozi',
    maintainer_email='dajiaozi@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'math_server = math_service_py.math_server:main',
        'math_client = math_service_py.math_client:main',
        ],
    },
)
