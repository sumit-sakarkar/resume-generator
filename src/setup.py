from setuptools import setup, find_packages

setup(
    name='resume-generation',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'numpy',
        'pandas',
    ],
)