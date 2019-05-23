#!/usr/bin/env python
# Copyright 2018 Chathuranga Abeyrathna. All Rights Reserved.
# AWS OpsWorks deployment cli

import sys
import getopt
import modules.common_functions


def common_help():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'h:v', [
            'help', 'version'])
    except getopt.GetoptError:
        modules.common_functions.usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            modules.common_functions.usage()
            sys.exit(0)
        elif opt in ('-v', '--version'):
            modules.common_functions.version()
            sys.exit(0)
        else:
            modules.common_functions.usage()
            sys.exit(0)
