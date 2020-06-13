from .version import version as __version__

import os as _os
for _s in ('algebra', 'combinatorics', 'data_structures', 'geometry', 
          'graphs', 'linear_algebra', 'numerical', 'strings', 'misc', 'tools'):
    __path__.append(_os.path.join(_os.path.dirname(__file__), _s))
