# encoding: utf-8

from setuptools import setup, find_packages, Command

version = '0.7.3'


class Unit2Discover(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys, subprocess
        basecmd = ['unit2', 'discover']
        errno = subprocess.call(basecmd)
        raise SystemExit(errno)


setup(
    name='locustio',
    version=version,
    description="Website load testing framework",
    long_description="""Locust is a python utility for doing easy, distributed load testing of a web site""",
    classifiers=[
        "Topic :: Software Development :: Testing :: Traffic Generation",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
    ],
    keywords='',
    author='Jonatan Heyman, Carl Bystrom, Joakim Hamrén, Hugo Heyman',
    author_email='',
    url='http://locust.io',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "gevent==1.1b6",
        "flask==0.10.1",
        "requests==2.8.1",
        "pyzmq==14.7.0"],
    tests_require=['unittest2', 'pyzmq'],
    entry_points={
        'console_scripts': [
            'locust = locust.main:main',
        ]
    },
    test_suite='unittest2.collector',
)
