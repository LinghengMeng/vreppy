from setuptools import setup
import os.path

def gen_data_files(*dirs):
    results = []

    for src_dir in dirs:
        for root,dirs,files in os.walk(src_dir):
            results.append((root, map(lambda f:root + "/" + f, files)))
    return results

setup(
    name='vreppy',
    packages=['vreppy', 'vreppy.vrep'],
    version='1.0.0',
    description='Simple python binding for V-REP robotics simulator',
    url='https://github.com/LinghengMeng/vreppy',
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
    ]
)
