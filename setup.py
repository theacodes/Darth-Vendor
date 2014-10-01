from setuptools import setup

VERSION = '0.0.2'

setup(
    name="darth",
    version=VERSION,
    author='Jon Wayne Parrott, [proppy], Michael R. Bernstein',
    author_email='jon.wayne.parrott@gmail.com, [proppy], michael@fandomhome.com',
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
    py_modules=['darth'],
    test_suite='nose.collector',
    install_requires=[
    ],
)
