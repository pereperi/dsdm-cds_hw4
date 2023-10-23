try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

import analysis_library


def get_requirements(requirements_path='requirements.txt'):
    with open(requirements_path) as fp:
        return [x.strip() for x in fp.read().split('\n') if not x.startswith('#')]


setup(
    name='analysis_library',
    version=analysis_library.__version__,
    description='Assignment 4 library with structure of classes',
    author='Pere, Alvaro, Sebastien',
    packages=find_packages(where='', exclude=['tests']),
    install_requires=get_requirements(),
    setup_requires=['pytest-runner', 'wheel'],
    url='https://github.com/pereperi/dsdm-cds_hw4',
    classifiers=[
        'Programming Language :: Python :: 3.10.7'
    ]
)