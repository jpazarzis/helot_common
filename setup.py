"""Setup for helot common library.

The setup is using implicit namespace packages from PEP 420 so exported
packages exported packages must be explicitly listed using the packages
parameter of the setup function ( find_packages will not work as expected
for more you can read here:
https://packaging.python.org/guides/packaging-namespace-packages/#native-namespace-packages

"""
from setuptools import setup

setup(
    name="helot_common",
    description="Exposes commonly reused functionality.",
    long_description="Exposes commonly reused functionality",
    url="https://github.com/jpazarzis/helot_common",
    author="John Pazarzis",
    install_requires=[
        "pyyaml",
    ],
    packages=["helot.common"],
    version='0.0.34',
)
