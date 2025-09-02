from setuptools import setup, find_packages

setup(
    name="phtnai_package",
    version="1.1.0",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
