from setuptools import setup, find_packages

with open('README.md', 'r') as fd:
    long_description = fd.read()

setup(
    name="PyRival",
    use_scm_version={
        "version_scheme": "post-release",
        "write_to": "pyrival/version.py"
    },
    url="https://github.com/cheran-senthil/PyRival",
    project_urls={
        "Bug Tracker": "https://github.com/cheran-senthil/PyRival/issues",
        "Documentation": "https://pyrival.readthedocs.io/",
        "Source Code": "https://github.com/cheran-senthil/PyRival",
    },
    author="Cheran Senthil",
    author_email="cheran.v.senthil@gmail.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    description="Competitive Programming Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["competitive-programming", "data-structures", "algorithms"],
    setup_requires=['setuptools_scm'],
    packages=find_packages(),
    entry_points={'console_scripts': ['interactive-runner=pyrival.tools.interactive_runner:main']},
)
