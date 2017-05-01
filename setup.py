# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages
from subprocess import Popen, PIPE


# Utility function to read the README.md file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README.md file and 2) it's easier to type in the README.md file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_hg_version():
    src_dir = os.path.dirname(os.path.abspath(__file__))
    output = Popen(["hg", "heads", "--template={rev}"], stdout=PIPE, cwd=src_dir).communicate()[0]
    return output


def get_git_tag():
    src_dir = os.path.dirname(os.path.abspath(__file__))
    output = Popen(["git", "describe", "--always"], stdout=PIPE, cwd=src_dir).communicate()[0]
    return output


setup(
    name="aliyun_api_ocr_python_wrap",
    version="%s" % get_git_tag(),
    author='twisker',
    description="a python wrap for using aliyun api OCR functionalities.",
    long_description=read('README.md'),
    packages=find_packages('.'),
    package_dir={'': '.'},
    package_data={
        '': [
        ],
    },
    requires=[
        "requests",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Software Industry",
        "License :: MIT License",
        "Natural Language :: Chinese (Simplified)",
        "Programming Language :: Python :: 2.7 - 3.6",
        "Topic :: Software Development",
    ],
)
