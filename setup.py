# setup.py
from setuptools import setup, find_packages

setup(
    name="random-ip-generator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "ipaddress",
    ],
    entry_points={
        "console_scripts": [
            "random-ip-generator=random_ip_generator.main:main",
        ],
    },
)