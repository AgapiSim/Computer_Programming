""" 
Student: Agapi Eleni Simaiaki
Date reviewed: 26/09/23
Part of the course: Computer programming II (1TD722)
Uppsala University
"""

"""
Data structures - Linear linked lists:

Instead of storing the records in a contiguous memory, we can let them point to each other
i.e. a record can contain the address of the next record. The advantage of this is that it 
is possible to link in new elements anywhere without moving already stored elements. One 
drawback is that the index operation requires Θ(n) operations because we have to start 
from the beginning and follow pointers until we come to elements with the sought index.

"""

#Conventionally the class are written in the beginNing of the code so that the code is more clearly wriTten and comprehensible
#Also since in the main() we create new linkedlist -> plist the class Person is not necessary to be written inside the LinkedList class

class Person:                     
    def __init__(self, name, pnr):
        self.name = name
        self.pnr = pnr

    def __str__(self):
        return f"{self.name}:{self.pnr}"

    def __lt__(self, new):
        return self.pnr < new.pnr

    def __le__(self, new):
        return self.pnr <= new.pnr

    def __eq__(self, new):
        return self.pnr == new.pnr


class LinkedList:

    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):            
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __in__(self, x):          
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    
    
    
    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')

    
    def remove(self, x):         
        """deletes the first node containing x as data. If
         the method finds a node with this content it should return True else False."""
         
        if self.first is None:
            return False #as asked in description  

        #x in the beginning of the list
        if self.first.data == x: 
            self.first = self.first.succ
            return True

        #check inside list if not 
        first = self.first
        while first.succ is not None: 
            if first.succ.data == x:
           
                first.succ = first.succ.succ
                return True
            first = first.succ

        return False  # Node with data 'x' not found in the list.

    

    #Method 2 of recursion - auxiliary function
    
    def to_list(self): 
        """which returns a standard Python list with
         the values from the linked list in the same order"""
         
        return self._to_list(self.first)

    def _to_list(self, node):
        if node is None:
            return []
        return [node.data] + self._to_list(node.succ) #concatenation of lists
        
 
#The method should return the number of removed nodes. 
#IMPORTANT IT RETURNS HOW MANY ELEMENTS ARE TO be REMOVED BUT IT DOESN'T UPDATE THE LINKED LIST


    def remove_all(self, x):  
        """removes all nodes which contains x as data. The method should return t
        he number of removed nodes"""
         
        return self._remove_all(self.first, x)

    def _remove_all(self, node, x):
        if node is None:
            return 0  # Base case: No nodes to remove in this branch

        count = self._remove_all(node.succ, x)  # Recursively remove nodes in the next branch

        if node.data == x:
            count += 1  # Increment count for each removed node
        #print(count)
        return count



    def __str__(self):         
        return '(' + self._to_str(self.first) + ')'

    
    def _to_str(self, node):
    """returns the list as a string of comma-separated values with 
     parentheses surrounding the list"""
     
        if node is None:
            return ''
        elif node.succ is None:
            return str(node.data)
        else:
            return str(node.data) + ', ' + self._to_str(node.succ)
    


    def copy(self):          
        """Rewrite the code so it gets a better complexity"""
        result = LinkedList()  # Create an empty linked list.
        
        for x in self:
            new_node = LinkedList.Node(x, None)  # Create a new node with the same data.
            if not result.first:                 # set the first node
                result.first = new_node
                last_result_node = new_node
            else:                                # update the rest nodes
                last_result_node.succ = new_node
                last_result_node = new_node

        return result

    ''' 
    Complexity of given code: quite a bit as it calls the insertion method for each element of the initial linked list
    Complexity for this implementation: iretation and copies without calling insert method for each elemnt of the initial listed node. O(#nodes)
    Also in the new approach mainly focusing on the nodes. ALso insertion and sorting doesn;t happen with the calling of the method but initially
    in the beggining on the main().

    '''


    def __getitem__(self, ind): 
        """Implement the index operator for linked lists"""
        current = self.first
        count = 0

        # go through linked list and keep track of the index.
        while current:
            if count == ind:
                return current.data  # return the element of the index
            current = current.succ #else proceed
            count += 1        
        pass



def main():
    lst = LinkedList()
    for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7]:
        lst.insert(x)   
    lst.print()

    print(lst.remove_all(1)) #prints the elements to be removed 


    
    print(str(lst))
    print(lst[2]) 
    
    #Person class testing
    plist = LinkedList()
    
    # create new objects
    p1 = Person("Agapi", 98)
    p2 = Person("Eleni", 723)
    p3 = Person("John", 4)

    # add new objects in plist | objects are inserted in the linked list sorted by the number (x - given second)
    plist.insert(p1)
    plist.insert(p2)
    plist.insert(p3) 
    plist.print()


'''
    #   if I insert the values in inversed then the sorting will occur based on the name but the printed outcome will be
    #   reversed as well 

    p4 = Person(98, "Agapi")
    p5 = Person(723, "Eleni")
    p6 = Person(4, "Ntina")

    plist.insert(p4)
    plist.insert(p5)
    plist.insert(p6)
    plist.print()
'''




if __name__ == '__main__':
    main()


'''

#this code passes the linked_list_test.py as it return the updated linked list after the removal with the removed elements and nodes.

    def remove_all(self, x):     # Compulsary
        self.first = self._remove_all(self.first, x)

    def _remove_all(self, node, x):
        if node is None:
            return None

        # skip every x
        while node is not None and node.data == x:
            node = node.succ

        # Continue recursively with the rest of the list.
        if node is not None:
            node.succ = self._remove_all(node.succ, x)

        return node


'''
