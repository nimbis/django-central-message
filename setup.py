from setuptools import setup, find_packages
from pip.req import parse_requirements
from uuid import uuid1

# parse requirements
reqs = parse_requirements("requirements/common.txt", session=uuid1())

# setup the project
setup(
    name="django-central-message",
    version="0.1.1",
    author="Nimbis Services, Inc.",
    author_email="info@nimbisservices.com",
    description="Wrapper for extends-messages to send to multiple users (all "
    "for now) from the admin page..",
    license="BSD",
    packages=find_packages(exclude=["tests", ]),
    install_requires=[str(x).split(' ')[0] for x in reqs],
    zip_safe=False,
    include_package_data=True,
    test_suite="tests.main",
)
