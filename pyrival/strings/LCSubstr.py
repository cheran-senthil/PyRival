from difflib import SequenceMatcher

LCSubstr = lambda a, b: SequenceMatcher(None, a, b).find_longest_match(0, len(a), 0, len(b))
