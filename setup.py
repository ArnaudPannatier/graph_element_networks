import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Graph Element Networks",
    version="1.0",
    author="Ferran Alet",
    author_email="ferran@deepmind.com",
    description="Graph Element Networks: adaptive, structured computation and memory",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FerranAlet/graph_element_networks",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)