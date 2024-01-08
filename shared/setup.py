import setuptools


setuptools.setup(
    name="python-aws-lambda-best-practices-shared",
    version="0.0.2",
    author="Ethan Hollins",
    author_email="ethan.hollins@shinesolutions.com",
    description="Shared Python library for the Python AWS Lambda best practices repo.",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "attrs",
        "cattrs",
        "jsonschema",
        "Werkzeug",
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
