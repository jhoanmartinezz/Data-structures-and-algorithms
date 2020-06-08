class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.tail = None

    def insertNode(self, newData):
        new_node = Node(newData)
        if self.tail is None:
            self.tail = new_node
        else:
            continue_node = self.tail
            while True:
                if continue_node.next is None:
                    break
                else:
                    continue_node = continue_node.next
            continue_node.next = new_node

    def printList(self):
        if self.tail is None:
            print("Empty list")
        else:
            currentNode = self.tail
            while True:
                if currentNode is None:
                    break
                else:
                    print(currentNode.data,"--->",currentNode.next)
                    currentNode = currentNode.next

list = linkedList()

list.insertNode("kira")
list.insertNode("milo")
list.insertNode("Merry")
list.insertNode("max")

list.printList()
