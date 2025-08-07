from setuptools import find_packages, setup


package_name = 'bev_cuda'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'pycuda', 'numpy', 'opencv-python'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='t25307@kist.re.kr',
    description='BEV Image Generator using CUDA from PointCloud2',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'bev_node = bev_cuda.bev_node:main'
        ],
    },
)

