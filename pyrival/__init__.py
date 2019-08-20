from .algebra import *
from .combinatorics import *
from .data_structures import *
from .geometry import *
from .graphs import *
from .linear_algebra import *
from .numerical import *
from .strings import *
from .version import version

__version__ = version

__all__ = (algebra.__all__ + combinatorics.__all__ + data_structures.__all__ + geometry.__all__ + graphs.__all__ +
           linear_algebra.__all__ + numerical.__all__ + strings.__all__)
