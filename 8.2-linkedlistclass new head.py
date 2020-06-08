class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def insertHead(self, newData):
        new_node = Node(newData)
        tempNode = self.head
        print("Temp node=",tempNode)
        self.head = new_node
        self.head.next = tempNode
        del tempNode

    def insertNode(self, newData):
        new_node = Node(newData)
        if self.head is None:
            self.head = new_node
        else:
            keep_node = self.head
            while True:
                if keep_node.next is None:
                    break
                else:
                    keep_node = keep_node.next
            keep_node.next = new_node

    def printList(self):
        if self.head is None:
            print("Empty list")
        actualNode = self.head
        while True:
            if actualNode is None:
                break
            print(actualNode.data,"Address-->",actualNode)
            actualNode = actualNode.next

list = linkedList()
list.insertNode("Kira 1")
list.insertNode("Kira 2")
list.insertNode("Kira 3")
list.printList()
list.insertHead("Nuevo nodo")
print("-"*20)
list.printList()
