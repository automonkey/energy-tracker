#!/usr/bin/env python
from glob import glob

from setuptools import find_packages, setup

setup(name='energy-tracker-build',
      description="Build and deployment utilities for Energy Tracker.",
      url='',
      author='Will Benyon',
      author_email='git@benyon.io',
      install_requires=[r.strip() for r in open("requirements.txt").readlines()],
      extras_require={
          'test': [r.strip() for r in open("test_requirements.txt").readlines()],
      },
      packages=find_packages(exclude=['*.test*']),
      zip_safe=False,
      entry_points={
          'console_scripts': [
              'energy-tracker-build = energy_tracker_build.src.cli:main',
          ]
      }
)
