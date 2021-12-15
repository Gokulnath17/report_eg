from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in gokul/__init__.py
from gokul import __version__ as version

setup(
	name="gokul",
	version=version,
	description="gokulnath",
	author="gokulnath",
	author_email="gokulnath@thirvusoft.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
