class XorBasis:
    " Linear basis for xor "
        
    def __init__(self):
        self.basis = []
    
    def insert(self, x):
        "Adds x to the basis if it is not redundant. Returns true if x is added to the basis"
        x = self._reduce(x)
        if x:
            self.basis.append(x)
        return x!=0
    
    def _reduce(self, x):
        for b in self.basis:
            x = min(x, x ^ b)
        return x
    
    def __len__(self):
        return len(self.basis)
    
    def __contains__(self, x):
        " Returns true if x can be represented as xor of some already inserted elements"
        return self._reduce(x)==0
    
    def __repr__(self):
        " Prints the basis in descending order "
        self.basis.sort(reverse=True)
        bit_length = max(self.basis).bit_length()
        repr_str = ""
        repr_str += "Basis:"
        for b in self.basis:
            repr_str+='\n'
            repr_str+= bin(b)[2:].zfill(bit_length)
        return repr_str