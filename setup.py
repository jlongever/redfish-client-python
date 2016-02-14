# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "on_http_redfish_1_0"
VERSION = "1.0.0"



# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.10", "six >= 1.9", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Redfish v1.0.0",
    author_email="",
    url="",
    keywords=["Swagger", "Redfish v1.0.0"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    
    """
)


