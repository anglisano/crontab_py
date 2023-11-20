import re
from setuptools import find_packages, setup
from cron_py._version import __version__

with open('requirements.txt', 'r') as req:
    requirements_list = [line.rstrip("\n") for line in req]

setup(
    name='cron_py',
    version=__version__,
    description='cron tab handler',
    author='Marc anglisano',
    author_email='marcanglisano@gmail.com',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "cron_py"},
    packages=find_packages(where="cron_py"),
    python_requires='>=3.8',
    license='',
)