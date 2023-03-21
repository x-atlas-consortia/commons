### Building and Publishing atlas-consortia-commons

<a href="https://pypi.org/project/setuptools/">SetupTools</a> and <a href="https://pypi.org/project/wheel/">Wheel</a> is required to build the distribution. <a href="https://pypi.org/project/twine/">Twine</a> is required to publish to Pypi

While at the root directory, build the distribution directory with: 

```bash
python3 setup.py sdist bdist_wheel
```

To publish, run:

```bash
twine upload dist/*
```

A prompt to enter login information to the hubmap Pypi account will appear


### Building and Publishing to Test

PyPI has a separate instance of the Python Package Index that allows you to try distribution tools and processes without affecting the real index located at [https://test.pypi.org/](https://test.pypi.org/).

Once you have built the distribution you can publish to this test instance with:

```bash
twine upload --repository testpypi dist/*
```

You can install this version with:

```bash
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps atlas-consortia-commons
```