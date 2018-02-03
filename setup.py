#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name="helot_configuration",
    description="Exposes a configuration object.",
    long_description="Exposes a configuration object.",
    url="https://github.com/jpazarzis/helot_configuration",
    author="John Pazarzis",
    install_requires=[
        "pyyaml",
    ],
    packages=find_packages(),
    version='0.0.1',
)
