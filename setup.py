from setuptools import setup, find_packages

# setup the project
setup(
    name="django-central-message",
    version="0.1.3",
    author="Nimbis Services, Inc.",
    author_email="info@nimbisservices.com",
    description="Wrapper for extends-messages to send to multiple "
                "users (all for now) from the admin page..",
    license="BSD",
    packages=find_packages(exclude=["tests", ]),
    install_requires=[
        'Django',
        'pytz >= 2014.2',
        'django-messages-extends >= 0.2',
    ],
    zip_safe=False,
    include_package_data=True,
)
