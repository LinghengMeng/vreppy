from setuptools import setup

setup(
    name='vreppy',
    packages=['vreppy', 'vreppy.vrep'],
    version='1.0.0',
    description='Simple python binding for V-REP robotics simulator',
    url='https://github.com/LinghengMeng/pyrep',
    author='Lingheng Meng',
    author_email='linghengmeng@yahoo.com',
    license='MIT',
    keywords='vrep robotics simulator binding api',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Topic :: Games/Entertainment :: Simulation',
        'Topic :: Education',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython'
    ],
    package_dir={'vreppy': 'scenes'},
    package_data={'vreppy': ['*.ttt']}
)
