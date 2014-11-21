from distutils.core import setup
setup(
  name = 'pybugs',
  packages = ['pybugs'], # this must be the same as the name above
  version = '0.1',
  description = 'Python library for finding common bugs and anti patterns',
  author = 'Christopher Harris',
  author_email = 'cbrentharris@gmail.com',
  url = 'https://github.com/cbrentharris/pybugs', # use the URL to the github repo
  download_url = 'https://github.com/cbrentharris/pybugs/tarball/0.1', # I'll explain this in a second
  keywords = ['testing', 'bugs', 'source code analysis'], # arbitrary keywords
  license='LICENSE.txt',
  install_requires=[
    "astunparse == 1.2.2",
  ],
  classifiers = [],
)