from setuptools import setup, find_packages

long_desc = """

"""


setup(
    name='wpget',
    version='0.1',
    description="Command line utility for retrieving a set of pages from Wikipedia.",
    long_description=long_desc,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        ],
    keywords='',
    author='Gregor Aisch',
    author_email='gregor.aisch@okfn.org',
    url='http://labs.okfn.org',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests','test.*']),
    namespace_packages=[],
    include_package_data=False,
    zip_safe=False,
    install_requires=["wikitools"],
    tests_require=[],
    entry_points={
        'console_scripts': [
             'wpget = wpget:cli'
        ]
    }
)
