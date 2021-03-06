import setuptools
from os import path as os_path

this_directory = os_path.abspath(os_path.dirname(__file__))


def read_file(filename):
    with open(os_path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


with open("README.md", "r") as fh:
    long_description = fh.read()


def read_requirements(filename):
    return [
        line.strip() 
        for line in read_file(filename).splitlines() 
        if not line.startswith('#')
    ]


setuptools.setup(
    name="pressure_test_lib",
    version="0.0.3",
    author="guanmengshi",
    description="压测包",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guanmengshi/test",
    keywords=['test', 'pressure-test'],
    packages=setuptools.find_packages(),
    install_requires=['aioredis>=1.1,<2'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
)
