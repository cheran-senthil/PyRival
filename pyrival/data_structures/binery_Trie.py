'''
The provided code defines a binary trie data structure
it can be used to represent a binary representation of numbers
The binary trie supports standard trie operations, such as adding and deleting values
enabling faster and more efficient computations compared to a traditional trie.
'''
class Node():
    def __init__(self):
        self.data=0
        self.left=None
        self.right=None
        self.count=0

class binTrie:
    def __init__(self,data=[]):
        self.root=Node()
        self.max_len=32 # Assuming 32-bit integers, can adjust based on requirements
        for i in data:
            self.add(i)
  
    def add(self,val):
        """
            Adds a value to the binary trie.
            time complexity is O(log n)
        """
        node=self.root
        for i in reversed(range(self.max_len)):
            bit = val & (1 << i)
            if bit:
                if not node.right:
                    node.right=Node()
                node=node.right
                node.count+=1
            else:
                if not node.left:
                    node.left=Node()
                node=node.left
                node.count+=1
        node.data=val
    def delete(self,val):
        """
        deletes a value from the binary trie 
        it should be contained in the trie
        time complexity is O(log n)
        """
        node=self.root
        for i in reversed(range(self.max_len)):
            bit = val & (1 << i)
            if bit:
                node=node.right
                node.count-=1
            else:
                node=node.left
                node.count-=1
                
    '''
    check if i can move to node 
    '''
    def check_L(self,node):
 
        return  node.left and node.left.count>0
    def check_R(self,node):
        return  node.right and node.right.count>0
    
    def max_xor(self, val):
        '''
        Find the maximum value obtained from performing bitwise XOR between the given value and any element of the trie.
        time complexity is O(log n)
        '''
        node = self.root
        for i in reversed(range(self.max_len)):
            bit = val & (1 << i)
            if bit:
                if  self.check_L(node):
                    node = node.left
                elif   self.check_R(node):
                    node = node.right
            else:
                if self.check_R(node):
                    node = node.right
                elif  self.check_L(node):
                    node = node.left
        max_result = max(val ^ node.data, val)
        return max_result
    
    def max_and(self, val):
        '''
        find the maximum value obtained from performing bitwise and  between given value and any element of the trie
        worst case time complexity is  ( 2^self.max_len)
        '''
        current_nodes=[self.root]
        for i in reversed(range(self.max_len)): 
            next_nodes=[]
            bit = val & (1 << i)
            for node in current_nodes:
                if bit and self.check_R(node):
                        next_nodes.append(node.right)
                else: 
                    if self.check_R(node):
                        next_nodes.append(node.right)
                    if  self.check_L(node):
                        next_nodes.append(node.left)
            current_nodes=next_nodes.copy()
        max_result = max(val & node.data for node in current_nodes)
        return max_result
        
    def max_or(self, val):
        '''
        find the maximum value obtained from performing bitwise or  between given value and any element of the trie
        worst case time complexity is  ( 2^self.max_len)
        '''
        current_nodes=[self.root]
        for i in reversed(range(self.max_len)): 
            next_nodes=[]
            bit = val & (1 << i)
            for node in current_nodes:
                if bit :
                    if self.check_L(node):
                        next_nodes.append(node.left)
                    if  self.check_R(node):
                        next_nodes.append(node.right)
                else:   
                    if   self.check_R(node):
                        next_nodes.append(node.right)
                    elif  self.check_L(node):
                        next_nodes.append(node.left)
            current_nodes=next_nodes.copy()
        max_result = max(val | node.data for node in current_nodes)
        return max_result
    
'''
# ---------
# how to use 
# ----------

trie=binTrie([5,6,4])

trie.add(7)
trie.add(2)
trie.add(3)

print(trie.max_xor(8))
print(trie.max_or(2))
print(trie.max_and(4))

trie.delete(7)
'''
