import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="aria2-json-rpc",
    version="0.0.3",
    author="Virace",
    author_email="Virace@yeah.net",
    description="a naive aria2c rpc api lib",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Virace/aria2-rpc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)