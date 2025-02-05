from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'My first Python package'
with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="jlmathlib", 
        version=VERSION,
        author="JesusLike",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=["mathlib"],
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
)