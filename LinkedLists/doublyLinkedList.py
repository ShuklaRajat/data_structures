#creates a simple node having value as dataval and nextval, and prevval field which points to None (or NULL) initially.
# But eventually prevval points to the previos node and nextval points to the next node.
# +_________+_________+_________+
# | prevval | dataval | nextval |
# +_________+_________+_________+
class Node:
        def __init__ (self, dataval = None):
                self.dataval = dataval
                self.next = None
                self.prev = None

# The below class performs all the DLL (Doubly Linked List) operations.
class DLL:
        def __init__(self):
            self.head = None
            self.tail = None

        #Traversing a DLL
        def printDLL(self):
                currPoint = self.head

                while currPoint:
                        print(currPoint.dataval)
                        currPoint = currPoint.next

        # def printReverseDLL(self):


#instantiate
dllInit = DLL()

#create independent nodes
n1 = Node("10")
n2 = Node("11")
n3 = Node("12")

#point head of the DLL to the first node
dllInit.head = n1
n1.prev = dllInit.head

#first node's nextVal points to the second node
n1.next = n2
n2.prev = n1
# ... and so on.
n2.next = n3
n3.prev = n2

#Testing the operations. (uncomment the code based on your use case).

#Traverse DLL
dllInit.printDLL()

# dllInit.printReverseDLL()