class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def insertNode(self, dataNode):
        new_node = Node(dataNode)
        if self.head is None:
            self.head = new_node
        else:
            continueNode = self.head
            while True:
                if continueNode.next is None:
                    break
                else:
                    continueNode = continueNode.next
            continueNode.next = new_node

    def deleteNodeAt(self, position):
        actual_node = self.head
        counter = 0
        while actual_node is not None:
            if position == counter:
                previousNode.next = actual_node.next
                actual_node.next = None
                break
            previousNode = actual_node
            actual_node = actual_node.next
            counter = counter + 1

    def size(self):
        head = self.head
        counter = 0
        while head is not None:
            counter = counter + 1
            head = head.next
        return counter

    def printList(self):
        if self.head is None:
            print("Empty list")
        else:
            currentNode = self.head
            while True:
                if currentNode is None:
                    break
                else:
                    print(currentNode.data,"--->",currentNode.next)
                    currentNode = currentNode.next
        print("Total nodes:",self.size())

list = linkedList()
list.insertNode("Liz")
list.insertNode("Kira")
list.insertNode("Milo")
list.insertNode("Merry")
list.printList()
list.deleteNodeAt(2)
print("*"*80)
list.printList()
