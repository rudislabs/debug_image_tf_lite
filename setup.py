from setuptools import setup

package_name = 'debug_image_tf_lite'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Benjamin Perseghetti',
    author_email='bperseghetti@rudislabs.com',
    maintainer='Benjamin Perseghetti',
    maintainer_email='bperseghetti@rudislabs.com',
    description='TF lite debug image.',
    license='BSD-3',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "debug_image_tf_lite_node = debug_image_tf_lite.debug_image_tf_lite_node:main"
        ],
    },
)
