from setuptools import setup, find_packages
import slacklog

setup(name='slacklog',
      version=slacklog.__version__,
      packages=find_packages(exclude=['tests']),
      install_requires=[
          'requests',
      ])
