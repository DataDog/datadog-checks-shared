# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

import os
import sys

from .validate import validate_py3


def main():
    """Run validate on a single python file"""
    if len(sys.argv) != 2:
        sys.stderr.write("No python file specified.\n")
        sys.stderr.flush()
        sys.exit(1)

    file_path = os.path.realpath(sys.argv[1].decode(sys.getfilesystemencoding()))
    if not os.path.exists(file_path):
        sys.stderr.write(u"{} does not exist.\n".format(file_path))
        sys.stderr.flush()
        sys.exit(1)

    results = validate_py3(file_path)
    if results:
        print(results[file_path])
