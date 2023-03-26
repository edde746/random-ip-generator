from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="random-ip-generator",
    version="0.1.1",
    author="edde746",
    description="A package to generate random IP addresses for a given country code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/edde746/random-ip-generator",
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
