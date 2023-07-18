'''
The code provided defines a binary trie data structure .
it can be used to represent a binary representation of numbers in a tree-like structure
so that it can be searched for in O(log n) time

It has methods to add and delete values from the tree, as well as 
(max_and, max_or, max_xor) with a given value

when dealing with binary numbers 
*** it better and faster than normal trie 

'''


class Node():
    def __init__(self):
        self.data=0
        self.left=None
        self.right=None
        self.count=0

class binTrie:
    def __init__(self,max_len=31):
        self.root=Node()
        self.max_len=max_len
  
    def add(self,val):
        """
            Adds a value to the binary trie.
        """
        temp=self.root
        for i in reversed(range(self.max_len)):
            bit = val & (1 << i)
            if bit:
                if not temp.right:
                    temp.right=Node()
                temp=temp.right
                temp.count+=1
            else:
                if not temp.left:
                    temp.left=Node()
                temp=temp.left
                temp.count+=1
        temp.data=val
    def delete(self,val):
        """
        deletes a value from the binary trie 
        it should be contained in the trie
        """

        temp=self.root
        for i in reversed(range(self.max_len)):
            bit = val & (1 << i)
            if bit:
                temp=temp.right
                temp.count-=1
            else:
                temp=temp.left
                temp.count-=1
                
    '''
    check if i can move to node 
    '''
    def check_L(self,node):
 
        return  node.left and node.left.count>0
    def check_R(self,node):
        return  node.right and node.right.count>0
    
    def max_and(self, val):
        '''
        find the maximum value obtained from performing bitwise and  between given value and any element of the trie
        time complexity is O(log n)
        '''

        q=[self.root]
        for i in reversed(range(self.max_len)): 
            temp_deque=[]
            bit = val & (1 << i)
            for temp in q:
                if bit and self.check_R(temp):
                        temp_deque.append(temp.right)
                else:
       
                    if self.check_R(temp):
                        temp_deque.append(temp.right)
                    if  self.check_L(temp):
                        temp_deque.append(temp.left)

            q=temp_deque.copy()

        return max( val & item.data for item in q )
        

    def max_or(self, val):
        '''
        find the maximum value obtained from performing bitwise or  between given value and any element of the trie
        time complexity is O(log n)
        '''
       
        q=[self.root]
        for i in reversed(range(self.max_len)): 
            temp_deque=[]
            bit = val & (1 << i)
            for temp in q:
                
                if bit :
                    if self.check_L(temp):
                        temp_deque.append(temp.left)
                    if  self.check_R(temp):
                        temp_deque.append(temp.right)
                else:
       
              
                    if   self.check_R(temp):
                        temp_deque.append(temp.right)
                    elif  self.check_L(temp):
                        temp_deque.append(temp.left)
            q=temp_deque.copy()

        return max( val |item.data for item in q )
    

    def max_xor(self, val):
        '''
        find the maximum value obtained from performing bitwise xor  between given value and any element of the trie
        time complexity is O(log n)
        '''
        temp = self.root
        for i in reversed(range(self.max_len)):
            bit = val & (1 << i)
            if bit:
                if  self.check_L(temp):
                    temp = temp.left
                elif   self.check_R(temp):
                    temp = temp.right
            else:
                if self.check_R(temp):
                    temp = temp.right
                elif  self.check_L(temp):
                    temp = temp.left
        return max(val ^ temp.data, val)
    
'''
# ---------
# how to use 
# ----------

trie=binTrie()

trie.add(7)
trie.add(2)
trie.add(3)

trie.delete(7)


print(trie.max_xor(8))
print(trie.max_or(2))
print(trie.max_and(4))
'''
