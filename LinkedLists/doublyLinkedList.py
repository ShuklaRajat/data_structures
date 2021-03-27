#creates a simple node having value as dataval and nextval, and prevval field which points to None (or NULL) initially.
# But eventually prevval points to the previos node and nextval points to the next node.
# +_________+_________+_________+
# |  prev   | dataval |  next   |
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

        def printReverseDLL(self):
            self.head, self.tail = self.tail, self.head

            currPoint = self.head

            while True:
                print(currPoint.dataval)
                currPoint = currPoint.prev
                if currPoint == self.tail:
                    print(currPoint.dataval)
                    break

        def insertAfter(self, afterValue, newData):
            newNode = Node(newData)

            currPoint = self.head
            while currPoint.next:
                if currPoint.dataval == afterValue:
                    break
                currPoint = currPoint.next
            newNode.next = currPoint.next
            currPoint.next = newNode

        #inserting value newData before the beforeValue (given as input)
        def insertBefore(self, beforeValue, newData):
                newNode = Node(newData)

                prevNode = self.head

                if prevNode is None:
                        return newNode

                currPoint = prevNode

                while currPoint.next:
                        if currPoint.dataval == beforeValue:
                                break
                        prevNode = currPoint
                        currPoint = currPoint.next

                newNode.next = currPoint
                prevNode.next = newNode



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

n3.next = dllInit.tail
dllInit.tail = n3
#Above operations generates the initial DLL.


#Testing the operations. (uncomment the code based on your use case).

dllInit.insertAfter("12", "12.5")
dllInit.insertBefore("12", "11.5")
#Traverse DLL
dllInit.printDLL()

# dllInit.printReverseDLL()