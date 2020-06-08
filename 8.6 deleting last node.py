class Node:
    def __init__(self, dataNode):
        self.data = dataNode
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def insertNodeEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            actualNode = self.head
            while True:
                if actualNode.next is None:
                    break
                else:
                    actualNode = actualNode.next
            actualNode.next = newNode

    def deleteNodeEnd(self):
        currentNode = self.head
        while currentNode.next is not None:
            beforNode = currentNode
            currentNode = currentNode.next
        beforNode.next = None

    def deleteNodeEnd(self):
        currentNode = self.head
        while currentNode.next is not None:
            beforeNode = currentNode
            currentNode = currentNode.next
        beforeNode.next = None

    def printList(self):
        if self.head is None:
            print("Empty list")
        else:
            currentNode = self.head
            while True:
                if currentNode is None:
                    break
                print(currentNode.data,"--->",currentNode.next)
                currentNode = currentNode.next

list = linkedList()
list.insertNodeEnd("Kira")
list.insertNodeEnd("milo")
list.insertNodeEnd("merry")
list.printList()
print("*"*80)
list.deleteNodeEnd()
list.printList()
