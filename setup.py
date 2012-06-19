from setuptools import setup, find_packages
import os

version = '0.1dev'

setup(name='collective.js.nivoslider',
      version=version,
      description="JQuery Nivogallery plugin as browser resource",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Espen Moe-Nillssen',
      author_email='espen@medialog.no',
      url='http://github.com/espenmn/collective.js.nivoslider',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.js'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
