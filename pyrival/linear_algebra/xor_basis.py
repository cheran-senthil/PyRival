class XorBasis:
    " Linear basis for xor "
        
    def __init__(self, bit_length=31):
        self.basis = []
        self.bit_length = bit_length
    
    def is_redundant(self, x):
        " Returns true if x can be represented as xor of some already inserted elements"
        
        return self._reduce(x)==0
    
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
        return self.is_redundant(x)
    
    def __repr__(self):
        " Prints the basis in descending order "
        print("Basis:")
        for b in self.basis:
            print(bin(b)[2:].zfill(self.bit_length))
        return ""
