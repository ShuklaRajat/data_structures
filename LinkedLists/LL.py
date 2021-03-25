#creates a simple node having value as dataval and nextval field which points to None (or NULL) initially.
# +_________+_________+
# | dataval | nextval |
# +_________+_________+
class Node:
        def __init__ (self, dataval = None):
                self.dataval = dataval
                self.nextval = None

# The below class performs all the SLL (Singly Linked List) operations.
class SLL:
        def __init__(self):
                self.head = None

        #Traversing a SLL
        def printSLL(self):
                currPoint = self.head

                while currPoint is not None :
                        print(currPoint.dataval)
                        currPoint = currPoint.nextval

        #inserting at the begining of SLL
        def insertAtBeginning(self, newData):
                newNode = Node(newData)
                newNode.nextval = self.head
                self.head = newNode

        #inserting at the begining of SLL
        def insertAtEnd(self, newData):
                newNode = Node(newData)

                if self.head is None:               #base condition.
                        self.head = newNode
                        return

                currPoint = self.head

                while currPoint.nextval:            #Traverse till end of the list
                        currPoint = currPoint.nextval

                currPoint.nextval = newNode

        #inserting value newData after the afterValue (given as input)
        def insertAfter(self, afterValue, newData):
                newNode = Node(newData)

                currPoint = self.head
                while currPoint.nextval:
                        if currPoint.dataval == afterValue:
                                break
                        currPoint = currPoint.nextval
                newNode.nextval = currPoint.nextval
                currPoint.nextval = newNode

        #inserting value newData before the beforeValue (given as input)
        def insertBefore(self, beforeValue, newData):
                newNode = Node(newData)

                prevNode = self.head

                if prevNode is None:
                        return newNode

                currPoint = prevNode

                while currPoint.nextval:
                        if currPoint.dataval == beforeValue:
                                break
                        prevNode = currPoint
                        currPoint = currPoint.nextval

                newNode.nextval = currPoint
                prevNode.nextval = newNode


#instantiate
sllInit = SLL()

#create independent nodes
n1 = Node("10")
n2 = Node("11")
n3 = Node("12")

#point head of the SLL to the first node
sllInit.head = n1

#first node's nextVal points to the second node
n1.nextval = n2
# ... and so on.
n2.nextval = n3

#Testing the operations. (uncomment the code based on your use case).

#Traverse SLL
# sllInit.printSLL()

#Insert a new node at beginning
# sllInit.insertAtBeginning("9")
# sllInit.insertAtBeginning("8")
# sllInit.printSLL()

#Insert a new node at end
# head1 = sllInit.insertAtEnd("13")
# sllInit.printSLL()

#Insert in after a given value
# sllInit.insertAfter("11", "11.5")
# sllInit.printSLL()

sllInit.insertAfter("12", "13")
sllInit.insertBefore("13", "11.75")
sllInit.printSLL()
