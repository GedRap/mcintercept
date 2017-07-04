from setuptools import setup

setup(
    name="mcintercept",
    version="0.1",
    description="Command line tool to intercept and analyze memcached traffic.",
    url="https://github.com/GedRap/mcintercept",
    author="Gediminas Rapolavicius",
    author_email="gediminas.rap@gmail.com",
    packages=["mcintercept"],
    install_requires=[
        "dpkt==1.8.8",
        "pypcap==1.1.5",
        "statsd==3.2.1"
    ],
    entry_points={
        'console_scripts': ['mcintercept=mcintercept.__main__:main'],
    }
)
