#!/bin/env python3

import sys

from setuptools import setup, find_packages

pack_name = 'webbed'

__version__ = '0.0.0'


def readme():
    with open('README.rst') as f:
        return f.read()

print('Current version: ', __version__)
version = __version__.split('.')


if sys.argv[-1] == 'minor':
    version[2] = str(int(version[2]) + 1)
    del sys.argv[-1]
elif sys.argv[-1] == 'major':
    version[1] = str(int(version[1]) + 1)
    version[2] = '0'
    del sys.argv[-1]
elif sys.argv[-1] == 'huge':
    version[0] = str(int(version[0]) + 1)
    version[1] = '0'
    version[2] = '0'
    del sys.argv[-1]


version = '.'.join(version)
with open(pack_name + '/version', 'w') as f:
    f.write(version)

setup(
    name=pack_name,
    packages=find_packages(),
    version=version,
    include_package_data=True,
    license='MIT',
    description='Allows the execution of python code within any file',
    long_description=readme(),
    author='Christoffer Zakrisson',
    author_email='christoffer_zakrisson@hotmail.com',
    # url='https://github.com/Zaeb0s/ez-crypt',
    keywords=['webbed', 'script', 'file'],
    classifiers=['Development Status :: 4 - Beta',
                 'Programming Language :: Python :: 3.5',
                 'Operating System :: POSIX :: Linux',
                 'License :: OSI Approved :: MIT License'],

    install_requires=[]
)


print('Installed version: ' + version)