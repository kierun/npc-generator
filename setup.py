# -*- coding: utf-8 -*-
"""
http://stackoverflow.com/questions/13529722/distribute-epydoc-and-setup-py
http://stackoverflow.com/questions/10130941/moving-from-epydoc-to-sphinx-to-auto-document-a-simple-python-py-file?rq=1
http://sphinx-doc.org/ext/autodoc.html
http://plone.org/documentation/kb/how-to-create-a-sphinx-based-documentation-for-your-project
http://pypi.python.org/pypi/modern-package-template
http://stackoverflow.com/questions/72852/how-to-do-relative-imports-in-python?lq=1


@note: Hack to prevent stupid error on exit of `python setup.py test` as
described here http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html.

"""
try:
    import multiprocessing
except ImportError:
    pass
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
from distutils.cmd import Command
from distutils.errors import DistutilsOptionError
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.1.0'

install_requires = [
    # List your project dependencies here.
    # For more details, see:
    # http://packages.python.org/distribute/setuptools.html#declaring-dependencies
]


class PyLint (Command):
    description = 'Runs pylint code checker.'
    user_options = []
    boolean_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run (self):
        from pylint import lint
        lint.Run(['src/npcgenerator/', 
            '--ignore=test', 
            '--include-ids=yes', 
            '--symbols=yes', 
            '--reports=no',
            ])



class PyTest(TestCommand):
    """
    http://pytest.org/latest/goodpractises.html
    """
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)



setup(name='npc_generator',
    version=version,
    description="NPC generator",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='RPG NPC Generator',
    author='Yann Golanski',
    author_email='npc-generator@kierun.org',
    url='',
    license='',
    packages=find_packages('src'),
    package_dir = {'': 'src'},include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts':
         ['npc_generator = npcgenerator.npc_generator:main']
    },
    tests_require=[
        'pytest>=2.3.4',
        'mock>=1.0.0',
        'pytest-cov>=1.6',
    ],
    cmdclass = {
        'test': PyTest,
        'pylint': PyLint,
    },
    package_data = {
        'npc_generator': ['brazilian_female_first_names.txt',
                          'brazilian_last_names.txt',
                          'brazilian_male_first_names.txt',
                          'cyberpunk.txt',
                         ]
    },
)
