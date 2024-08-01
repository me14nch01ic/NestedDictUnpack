from setuptools import setup, find_packages

setup(
    name='NestedDictUnpack',
    version='0.1.0',
    description='A utility to unpack nested dictionaries',
    author='me14nch01ic',
    author_email='mindtraveller11@gmail.com',
    url='https://github.com/me14nch01ic/NestedDictUnpack',
    packages=find_packages(),
    install_requires=[],
    dependency_links=[
        'git+https://github.com/me14nch01ic/NestedDictUnpack.git#egg=NestedDictUnpack'
    ],
    classifiers=[],
    python_requires='>=3.6',
)