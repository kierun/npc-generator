#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Main entry point.

    >>> ipython -i -c "%run ./npc_generator.py -n brazilian -s cyberpunk"
    >>> python ./npc_generator.py -n brazilian -s cyberpunk

"""
__major__ = 0
__minor__ = 1
__patch__ = 0
__version__ = '%d.%d.%d' % (__major__, __minor__, __patch__)
import optparse
import sys
import os
import time
import random
random.seed(time.mktime(time.gmtime()))
from npcgenerator.NPC import NPC


def main():
    parser = optparse.OptionParser(version=__version__)
    parser.add_option("-s", "--skills", dest="file_skills", default=None,
                      help="A file containing a lists of skills [Optinal].", metavar="STR")
    parser.add_option("-n", "--names", dest="file_names", default=None,
                      help="A file prefix to files containing a lists of names.",
                      metavar="STR")
    (options, args) = parser.parse_args(sys.argv)
    if options.file_names is None:
        sys.stderr.write('ERROR:  No name prefix, cannot continue.\n')
        sys.exit(1)
    here = os.path.dirname(__file__)
    if options.file_skills is not None:
        obj = NPC(
            os.path.join(
                here, 'data', options.file_names + '_male_first_names.txt'),
            os.path.join(here, 'data',
                               options.file_names + '_female_first_names.txt'),
            os.path.join(
                here, 'data', options.file_names + '_last_names.txt'),
            os.path.join(here, 'data', options.file_skills + '.txt'))
    else:
        obj = NPC(
            os.path.join(
                here, 'data', options.file_names + '_male_first_names.txt'),
            os.path.join(here, 'data',
                               options.file_names + '_female_first_names.txt'),
            os.path.join(here, 'data', options.file_names + '_last_names.txt'))
    obj.get_new_data()
    print obj.get_markdown()


if __name__ == "__main__":
    main()
    sys.exit(0)
