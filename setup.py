#!/usr/bin/env python
from setuptools import setup

# The setup is using implicit namespace packages from PEP 420 so exported
# packages exported packages must be explicitly listed using the packages
# parameter of the setup function ( find_packages will not work as expected
# for more you can read here:
# https://packaging.python.org/guides/packaging-namespace-packages/#native-namespace-packages
#


setup(
    name="helot_configuration",
    description="Exposes a configuration object.",
    long_description="Exposes a configuration object.",
    url="https://github.com/jpazarzis/helot_configuration",
    author="John Pazarzis",
    install_requires=[],
    packages=["helot.configuration"],
    version='0.0.313',
)
