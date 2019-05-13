import textwrap

from setuptools import setup

from pytest_circleci import __version__

setup(
    name="patreon-pytest-circleci",
    version=__version__,
    description="py.test plugin for CircleCI",
    long_description = textwrap.dedent("""
    Use CircleCI env vars to determine which tests to run

    - CIRCLE_NODE_TOTAL indicates total number of nodes tests are running on
    - CIRCLE_NODE_INDEX indicates which node this is

    Will run a subset of tests based on the node index.

    """),
    author="Michael Twomey",
    author_email="mick@twomeylee.name",
    url="https://github.com/Patreon/pytest-circlci",
    packages=["pytest_circleci"],
    install_requires=[
        'pytest',
    ],
    entry_points={
        'pytest11': [
            'circleci = pytest_circleci.plugin'
        ],
    },
    classifiers=(
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ),
)
