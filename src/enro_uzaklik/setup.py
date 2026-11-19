from setuptools import find_packages, setup

package_name = 'enro_uzaklik'

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
    maintainer='vboxuser',
    maintainer_email='macit24@itu.edu.tr',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'uzaklik_sunucu = enro_uzaklik.uzaklik_sunucu:main',
            'uzaklik_istemci = enro_uzaklik.uzaklik_istemci:main',
        ],
    },
)
