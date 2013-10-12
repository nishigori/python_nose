# -*- coding: utf-8 -*-
try:
    from setuptools import setup, Command
except ImportError:
    from distutils.core import setup, Command


setup(
    name='The skeleton of nose for python users.',
    version='0.0.1',
    url='https://github.com/tddbc/python_nose',
    author='TDD Base Camp',
    author_email='tddbc@googlegroups.com',
    description='The skeleton of nose for python users',
    license='MIT',
    packages=[],
    package_data={},
    scripts=[''],
    setup_requires=['nose>=1.0'],
    test_suite='nose.collector',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
