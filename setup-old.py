# See: https://github.com/pr3d4t0r/ipwhere/blob/master/LICENSE.txt


import pathlib
import sys

from setuptools import find_packages
from setuptools import setup

from ipwhere import __VERSION__

# +++ constants +++

HERE = pathlib.Path(__file__).parent
README = (HERE / 'README.md').read_text()


# *** functions ***

def readToList(fileName):
    return [line.strip() for line in open(fileName).readlines()]


# *** main ***

if '__main__' == __name__:
    requirements = readToList('requirements.txt')

    setup(
        author                        = 'Eugene Ciurana pr3d4t0r',
        author_email                  = 'ipwhere.project@cime.net',
        classifiers                   = [
            "Intended Audience :: Other Audience",
            "License :: OSI Approved :: BSD License",
            "Operating System :: MacOS",
            "Operating System :: Unix",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.9",
            "Topic :: System :: Archiving :: Backup",
            "Topic :: Utilities",
        ],
        description                   = 'ipwhere - query an IP address geographical location',
        entry_points                  = {
                                    'console_scripts': {
                                        'ipwhere=ipwhere:main',
                                    }
                               },
        include_package_data          = True,
        install_requires              = requirements,
        license                       = "BSD3",
        long_description              = README,
        long_description_content_type = 'text/markdown',
        name                          = open('package.txt').read().replace('\n', ''),
        namespace_packages            = [ ],
        packages                      = find_packages(),
        url                           = 'https://github.com/pr3d4t0r/ipwhere',
        version                       = __VERSION__,
    )

sys.exit(0)

