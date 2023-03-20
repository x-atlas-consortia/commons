from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="consortia-commons",
    version="1.0.3",
    author="Atlas Consortia",
    author_email="api-developers@hubmapconsortium.org",
    description="The common code supporting the web services in the consortia.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/x-atlas-consortia/commons",
    packages=['consortia_commons',
              'consortia_commons.rest',
              'consortia_commons.ubkg',
              'consortia_commons.file',
              'consortia_commons.string',
              'consortia_commons.object'],
    package_data={'': ['*.json']},
    include_package_data=True,
    install_requires=[
        'Flask>=2.1.3',
        # For now use pinned version of jsonref due to breaking changes made in 1.0.0
        'jsonref==0.3.0',
        'jsonschema>=3.2.0',
        'neo4j>=4.2.1',
        'pytz>=2021.1',
        'property>=2.2',
        # Airflow dependes on globus_sdk==1.9.0
        'globus_sdk>=1.9.0',
        # cwltool uses prov==1.5.1
        # Will remove provenance.py and this prov dependency later
        'prov>=1.5.1',
        # It's an agreement with other collaborators to use the beblow versions
        # for requests and PyYAML
        'requests>=2.22.0',
        'PyYAML>=5.3.1'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        # "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
)
