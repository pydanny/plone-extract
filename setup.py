from setuptools import setup, find_packages
 
version = '0.1.0'
 
setup(
    name='plone-extract',
    version=version,
    description="Slurps out data from Plone sites into JSON.",
    long_description=open("README.rst").read(),
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
