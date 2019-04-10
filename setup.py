from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

classifiers = [
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'License :: OSI Approved :: MIT License',
    'Topic :: Utilities']

setup(name='annotated-images',
      version='0.1.0',
      description='Split training data images into training, validation and test (dataset) folders.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/saberd/split-folders',
      author='saberd',
      author_email='mail@saberd.com',
      license='MIT',
      packages=['annotated-images'],
      classifiers=classifiers)