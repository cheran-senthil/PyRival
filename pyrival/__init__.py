from .version import version as __version__

import os as _os
for s in ('algebra', 'combinatorics', 'data_structures', 'geometry', 
          'graphs', 'linear_algebra', 'numerical', 'strings', 'misc', 'tools'):
    __path__.append(_os.path.join(__path__[0], s))
