from setuptools import setup, find_packages

setup(
    name='badcode_utilities',
    version='0.1.2',  # or higher, must be unique and not used before
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'badcode_utilities': ['badwords.txt'],
    },
    install_requires=[
        # none
    ]
)