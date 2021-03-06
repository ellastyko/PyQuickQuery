#!/usr/bin/env python3
from setuptools import setup, find_packages

version = "0.0.1"

with open("./README.rst", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="PyQuickQuery",
    version=version,
    url="https://github.com/ellastyko/quickquery",
    project_urls={
        "Documentation": "https://",
    },
    description="SQL query builder",
    long_description=readme,
    packages=find_packages(exclude=["tests*", "pymysql.tests*"]),
    python_requires=">=3.6",
    extras_require={},
    classifiers=[
        "Development Status :: 5 - Development",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Database",
    ],
    keywords="Query",
)