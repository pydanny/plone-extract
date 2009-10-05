from setuptools import setup, find_packages
 
version = '0.1.0'
 
LONG_DESCRIPTION = """
=============
Plone Extract
=============

A common use case in Plone is content extraction. Either to another Plone site
or to another framework. Existing Plone export methods are either incomplete or
rely heavily on complex XML structures. This project will focus on keeping
things simple and easy. 
"""
 
setup(
    name='plone-extract',
    version=version,
    description="Slurps out data from Plone sites into JSON.",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Plone",
        "Environment :: Web Environment",
    ],
    keywords='',
    author='Daniel Greenfeld',
    author_email='pydanny@gmail.com',
    url='http://github.com/pydanny/plone-extract/tree/master',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    setup_requires=['setuptools_git'],
)
