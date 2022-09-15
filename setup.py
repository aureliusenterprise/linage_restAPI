from setuptools import find_packages, setup

setup(
    name="m4i-linage-rest-api",
    version="1.0.0",
    url="https://github.com/aureliusenterprise/linage_restAPI",
    author="Aurelius Enterprise",
    packages=find_packages(),
    install_requires=[
        "Flask",
        "requests",
        "pandas",
        "SQLAlchemy",
        "flask-restx",
        "MarkupSafe==2.0.1",
        "msgpack",
        "ujson",
        "m4i_atlas_core"

    ],
    zip_safe=False
)
