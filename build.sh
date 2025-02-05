# provide repository credentials
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=$(cat secrets/pypi_token)

# install requirements
pip install --upgrade pip
pip install setuptools
pip install wheel

# cleanup
rm -rf ./build
rm -rf ./dist
rm -rf ./jlmathlib.egg-info

# build local distribution
python setup.py sdist bdist_wheel

# push into test repository
twine upload --repository testpypi dist/*