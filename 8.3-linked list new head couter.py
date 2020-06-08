class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList():
    def __init__(self):
        self.head = None

    def insertNode(self,newData):
        new_node = Node(newData)
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

    def sizeList(self):
        count = 0
        current = self.head
        while current:
            count = count + 1
            current = current.next
        return count

    def newHead(self, dataHead):
        newHead = Node(dataHead)
        temp = self.head
        self.head = newHead
        newHead.next = temp
        del temp

    def newTail(self, dataTail):
        new_tail = Node(dataTail)
        if self.head.next is None:
            self.head.next = new_tail

    def counterList(self):
        self.size = self.size + 1
        return self.size

    def printList(self):
        if self.head is None:
            print("Empty list")
        else:
            actual_node = self.head
            while True:
                if actual_node.next is None:
                    print(actual_node.data,"--->",actual_node.next)
                    break
                else:
                    print(actual_node.data,"--->",actual_node.next)
                    actual_node = actual_node.next
            print("Linked list contains:",self.sizeList(),"nodes")

list = linkedList()

list.insertNode("Kira")
list.insertNode("Milo")
list.insertNode("Merry")
list.newHead("new head")
list.printList()
list.sizeList()
