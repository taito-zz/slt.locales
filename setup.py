from setuptools import find_packages
from setuptools import setup


setup(
    name='slt.locales',
    version='0.3.1',
    description="Overrides default translations for SLT site.",
    long_description=open("README.rst").read(),
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"],
    keywords='',
    author='Taito Horiuchi',
    author_email='taito.horiuchi@abita.fi',
    url='https://github.com/taito/slt.locales',
    license='None-free',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['slt'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'sll.baselocales'],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """)
