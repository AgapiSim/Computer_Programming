""" 
Student: Agapi Eleni Simaiaki
Mail: agapi-eleni.simaiaki.4287@student.uu.se
Part of the course: Computer programming II (1TD722)
Uppsala University
"""

"""
Binary Tree structures:

Here a structure for storing nodes in binary search trees is built. In the code, the stored
records are names keys and use integers as an example, but all types of data that have the
order relations defined works well. The same key is not allowed to occur multiple times.
At a minimum, we want to be able to create trees, add new records, search for certain
records and print the contents of the tree.
The code uses Linked_List.py file.
"""

from Linked_List import LinkedList


class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # in-order traversal | finds all nodes and 
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Dicussed in the text on generators
        if self.root:
            yield from self.root #iteration that is based on the __iter__() of the Node class

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key): #! inserts elements based on binary search trees | creates nodes as well
        if r is None:
            return self.Node(key) #tra
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k):
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)




    def height(self):                            
        #returns the height of the tree
        return self._height(self.root)

    def _height(self, r):
        if r is None:
            return 0
        else:
            r_side = 1 + self._height(r.right)  
            l_side = 1 + self._height(r.left)               
        if r_side >= l_side:
            return r_side
        return l_side



    def remove(self, key):                    # 
        #Removal of nodes - acts on the key which has been created by the Node class
        self.root = self._remove(self.root, key)

    def _remove(self, r, k):                      
        #print(r)
        if r is None:
            return None
        elif k < r.key:
            r.left = self._remove(r.left, k)                          # r.left = left subtree with k removed
        elif k > r.key:
            r.right = self._remove(r.right, k)                        # r.right =  right subtree with k removed
        
        else:  
            # Easy case | one child or no child
            if r.left is None:     
                return r.right
            elif r.right is None: 
                return r.left 
            
            # Tricky case | Node with two children
            else:  
                
                min_node = r.right                                    # Find the smallest key in the right subtree
                while min_node.left is not None:
                    min_node = min_node.left

                r.key = min_node.key                                  # Put that key in this node
                r.right = self._remove(r.right, min_node.key)         # Remove that key from the right subtree
                
        return r  # Remember this! It applies to some of the cases above




    def __str__(self): 
        """elements in the string are returned separated by commas followed by a space 
           and the string are surrounded by ’<’ and ’>’
        """
        elem = iter(self)
        return f"<{', '.join(str(e) for e in elem)}>"




    def to_list(self):     
        """which creates and returns a standard Python list with the values from the tree"""
        return list(iter(self))
        #The complexity is O(n) for the iteration (n is the number of elements) - the addition of each element to list instant for all 




    def to_LinkedList(self):  
        """ creates and returns a LinkedList with the values from the tree """
        l_list = LinkedList() #creat linked list

        for k in self: 
            l_list.insert(k)  # insert one key at a time

        return l_list
        
    # O(n^2) due to traversing and for-loop combo




    def ipl(self): 
        """calculates and returns the internal path length"""
        return self._ipl(self.root, 1) #root has level 1

    def _ipl(self, node, level):
        if node is None:
            return 0
        left_ipl = self._ipl(node.left, level + 1)
        right_ipl = self._ipl(node.right, level + 1)
        return level + left_ipl + right_ipl
        #parallel traversing right and left side adding to the level



    
#Generation of random trees
def random_tree(n):                               
    bst = BST()
    for x in range(n):
        key = random.random()
        bst.insert(key)
    return bst


import random
import math

def main():
    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)
    t.print()
    

    print('size  : ', t.size())
    for k in [0, 1, 2, 5, 9]:
        print(f"contains({k}): {t.contains(k)}")

    print(str(t))

    t.remove(5)
    print(t)

    sizes = [100, 200, 800, 4000, 8000, 12000, 160000 ]  #when log2 is a good idea to change by doubling
    for n in sizes:
        #create various random trees per iteration
        tree = random_tree(n)
        #print(tree)
        #calculate observed ipl and height
        observed_ipl = tree.ipl()
        observed_height = tree.height()

        #calculate theoretical-expected ipl formula: 1.39n log₂(n) + O(n)
        expected_ipl = 1.39 * n * math.log2(n) + n

        print(f"Number of nodes: {n}")
        print(f"Observed Height: {observed_height}")
        print(f"Observed IPL/n : {observed_ipl/n}")
        print(f"Expected IPL/n : {expected_ipl/n}\n")


if __name__ == "__main__":
    main()


"""

Theoretical exercise: Experimentally verify that the internal path length (ipl) grows as
                      1.39n log2 (n) + O(1) in trees built up with random numbers. At the same time, 
                      try to see how the height seems to depend on the number of nodes.
====================================================================================================    

            They seem to be quite close with a constant minor deviation.
            There constantly seems to be a deviation between the estimated ipl and the observed ipl. 
            The estimated ipl seems to constantly be larger than the observed. That might be due to
            randomization of the selection of the elements of the tree. When the elements are randomly
            selected the insertion process might lead to trees with longer branches out of chance and 
            large ipl or even short branches and small ipl.

            The height of the trees seems to increase as the size of the tree and nodes is increased. 
            No obvious rate of increase is seen between the size and the height of a tree.



Theoretical exercise: What is the generator good for?
=====================================================

1. computing size?     Yes, going through the nodes and adding them 
2. computing height?   Yes it could be used to check the nodes per side but recursively there no need of direct traversal search
3. contains?           Yes, going through the tree to comparing keys to the one we search
4. insert?             Not direclty helpful in the insertion. Might be useful in scanning the tree to identify the location
5. remove?             Not directly helpful in the removal. Might be useful in scanning the tree to identify the location




Results for ipl of random trees (Exercise 20)
============================================

Number of nodes: 100
Observed Height: 14
Observed IPL/n : 8.38
Expected IPL/n : 10.234960103786868

Number of nodes: 200
Observed Height: 18
Observed IPL/n : 9.255
Expected IPL/n : 11.624960103786867

Number of nodes: 800
Observed Height: 20
Observed IPL/n : 12.6025
Expected IPL/n : 14.404960103786868

Number of nodes: 4000
Observed Height: 30
Observed IPL/n : 15.2275
Expected IPL/n : 17.632440155680303

Number of nodes: 8000
Observed Height: 29
Observed IPL/n : 15.99925
Expected IPL/n : 19.022440155680304

Number of nodes: 12000
Observed Height: 31
Observed IPL/n : 17.329833333333333
Expected IPL/n : 19.835538031682706

Number of nodes: 160000
Observed Height: 40
Observed IPL/n : 21.3591375
Expected IPL/n : 25.02992020757373

"""
