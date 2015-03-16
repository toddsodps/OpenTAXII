from os.path import join, dirname
from setuptools import setup, find_packages

CURRENT_DIR = dirname(__file__)

def get_file_contents(filename):
    with open(join(CURRENT_DIR, filename)) as fp:
        return fp.read()

setup(
    name = "opentaxii",
    description = "Intelworks TAXII server implementation",
    long_description = get_file_contents('README.rst'),
    url = "https://github.com/Intelworks/OpenTAXII",
    author = "Intelworks",
    author_email = "opentaxii@intelworks.com",
    version = "0.0.2",
    license="BSD License",
    packages = find_packages(),
    include_package_data = True,
    package_data = {
        'opentaxii' : ['*.yml']
    },
    install_requires = [
        'libtaxii==1.1.105-SNAPSHOT',
        'pytz==2014.10',
        'intelworks-common',
        'pyyaml',
        'anyconfig',
        'structlog',
        'Flask',
        'sqlalchemy',
        'blinker',
        'gunicorn',
        'redis'
    ],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)