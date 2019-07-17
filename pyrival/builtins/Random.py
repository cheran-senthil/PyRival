import sys

hashlib = sys
hashlib.__dict__["sha512"] = None
sys.modules["hashlib"] = hashlib
import random
