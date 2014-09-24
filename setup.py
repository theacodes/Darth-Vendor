from setuptools import setup

VERSION = '0.0.1'

setup(
    name="darth",
    version=VERSION,
    author='Jon Wayne Parrott, [proppy], [webmaven]',
    author_email='jjramone13@gmail.com, [proppy], [webmaven]',
    maintainer='Jon Wayne Parrott',
    maintainer_email='jon.wayne.parrott@gmail.com',
    description='Third-party vendoring helper for Google App Engine and other sandboxed python environments.',
    url='https://github.com/jonparrott/Darth-Vendor',
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
    ],
    packages=['darth'],
    test_suite='nose.collector',
    install_requires=[
    ],
)
