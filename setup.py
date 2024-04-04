from setuptools import find_packages, setup

from chartz import __version__

setup(
    name="chartz",
    version=__version__,
    description="Simple python wrapper for echarts",
    long_description=open("README.md").read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.11",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=["echarts", "charts"],
    author="Nathan Johnson, Austin Sauer & Wesley Howery",
    author_email="info@stratusadv.com",
    url="https://github.com/stratusadv/chartz",
    license="MIT",
    packages=find_packages(exclude=["docs"]),
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.11",
)
