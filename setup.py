import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="al_filemodules",
    version="1.0.0",
    author="AdamantLife",
    author_email="",
    description="A Collection of filesystem utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AdamantLife/AL_Filemodules",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        
        ]
)
