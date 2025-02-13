# My First Python Package

- install package build tool

```
pip install setuptools wheel
```

## build & install & test

```
# build
python setup.py sdist bdist_wheel

# install new package to local, if success
pip install dist/my_package-0.0.1-py3-none-any.whl

# run test code
python test/test.py
```