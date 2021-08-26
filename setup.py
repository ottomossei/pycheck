
from setuptools import setup, find_packages

with open('requirements.txt') as requirements_file:
    install_requirements = requirements_file.read().splitlines()

setup(
    name="pycheck",
    version="1.0.3",
    description="A Python tool that mainly supports unit testing.",
    author="ottomossei",
    author_email="seki.jobhunting@gmail.com",
    install_requires=install_requirements,
    url='https://github.com/ottomossei/checkpy/',
    license=license,
    packages=find_packages("pycheck")
)