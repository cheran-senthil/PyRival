class XorBasis:
    " Linear basis for xor "
        
    def __init__(self, bit_length=31):
        self.bit_length=bit_length
        self.basis_size=0
        self.val = [0]*self.bit_length
    
    def is_redundant(self, x):
        " Returns true if x can be represented as xor of some already inserted elements"
        
        for i in range(self.bit_length):
            if (x>>i)&1:
                if self.val[i]==0:
                    return False
                x^=self.val[i]
        return True
    
    def insert(self, x):
        "Adds x to the basis if it is not redundant. Returns true if x is added to the basis"
        for i in range(self.bit_length):
            if (x>>i)&1:
                if self.val[i]==0:
                    self.val[i]=x
                    self.basis_size+=1
                    return True
                x^=self.val[i]
        return False
    
    def __len__(self):
        return self.basis_size
    
    def __getitem__(self, i):
        return self.val[i]
    
    def __contains__(self, x):
        return self.is_redundant(x)
    
    def __repr__(self):
        " Prints the basis in descending order "
        print("Basis:")
        for i in range(self.bit_length-1, -1, -1):
            if self.val[i]!=0:
                print(bin(self.val[i])[2:].zfill(self.bit_length))
        return ""
