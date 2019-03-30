""" Python 3 compatibility tools. """
from __future__ import division, print_function

import sys

if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip
