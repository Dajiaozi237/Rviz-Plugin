from setuptools import find_packages, setup

package_name = 'demo_python'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dajiaozi',
    maintainer_email='3373469120@qq.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
             'service = demo_python.service_member_function:main',
             'client = demo_python.client_member_function:main',
        ],
    },
)
