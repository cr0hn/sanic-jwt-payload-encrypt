import re

from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'requirements.txt')) as f:
    required = f.read().splitlines()

with open(path.join(here, 'sanic_jwt_payload_encrypt', '__init__.py')) as f:
    version = re.search(
        r'(__version__)([\s]*=[\s]*\")([\d\.]+)', f.read()
    ).group(3)

setup(
    version="1.0.1",
    install_requires=required,
)