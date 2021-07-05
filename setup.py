from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["pandas>=1.2"]

setup(
    name="bacen",
    version="0.9.3",
    author="Bernardo Paulsen",
    author_email="bernardopaulsen@gmail.com",
    description="A package to import data frmo BACEN's Time Series Management System",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/bernardopaulsen/bacen",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
    ],
)