from setuptools import setup, find_packages

setup(
    name="prism_viewer",
    version="0.1.1",
    author="Kajal_Halani",
    description="A PyQt5 and PythonOCC-based 3D rectangular prism viewer application",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/anuranjani23/fossee-3D-rectangular-prism-viewer",
    license="MIT",
    packages=find_packages(where="."),
    package_dir={"prism_viewer": "prism_viewer"},
    include_package_data=True,
    install_requires=[
        "numpy==2.2.6",
        #"swig",
        #"pythonocc-core==7.9.0",
        "pyqt5==5.15.11",
        "six==1.17.0",
        "svgwrite",
    ],
    entry_points={
        "console_scripts": [
            "prism_viewer=prism_viewer.main:main",
        ],
    },
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    test_suite="prism_viewer.tests",
)
