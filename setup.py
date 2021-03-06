from setuptools import setup, find_packages

version = '0.1.2'

setup(name='oc-tt',
      version=version,
      description="OpenCore Software TaskTracker client package",
      long_description="""\
""",
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Plugins",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Office/Business :: Office Suites",
        "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='OpenCore Software TaskTracker client',
      author='The Open Planning Project',
      author_email='opencore-dev@lists.coactivate.org',
      url='https://github.com/socialplanning/oc-tt',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['opencore'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'oc-cab'
      ],
      entry_points="""
      # -*- Entry points: -*-
      [opencore.versions]
      oc-tt = opencore.tasktracker
      [topp.zcmlloader]
      opencore = opencore.tasktracker
      """,
      )
