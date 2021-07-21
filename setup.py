# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 14:35:27 2021

@author: sophi
"""

# setup file

from setuptools import setup

# read README
with open('README.md') as readme_file:
    README = readme_file.read()

# setup args
setup_args = dict(
      name = "pip_test",
      version = "0.1",
      license = "MIT",
      description = "Scrapes summary data from all gmap locations",
      long_description = README,
      url = "http://github.com/sophiahill/pip_test",
      author = "Basil Labs",
      author_email = "sghill@andrew.cmu.edu",
      packages = ["pip_test"],
      include_package_data = True,
      zip_safe = True
)

# requirements
install_requires = [
      "pandas==1.0.4",
      "tqdm==4.49.0",
      "selenium==3.141.0",
      "numpy==1.19.5",
      "webdriver_manager==3.4.2",
      "path.py==12.5.0",
      "progressbar33==2.4"
]

if __name__ == "__main__":
      setup(**setup_args, install_requires = install_requires)