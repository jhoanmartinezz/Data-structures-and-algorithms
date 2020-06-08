class Node:
    def __init__(self,data):
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
            continue_node = self.head
            while True:
                if continue_node.next is None:
                    break
                else:
                    continue_node = continue_node.next
            continue_node.next = new_node

    def insertNewHead(self, dataHead):
        node_head = Node(dataHead)
        tempNode = self.head
        self.head = node_head
        node_head.next = tempNode
        del tempNode

    def insertBetween(self, positionDesired, dataBetween):
        node_between = Node(dataBetween)
        if positionDesired == 0:
            self.insertNewHead(dataBetween)
            return
        if positionDesired > self.listSize():
            print("Invalid position")
        counter = 0
        actualNode = self.head
        while actualNode != None:
            if counter == positionDesired:
                beforeNode.next = node_between
                node_between.next = actualNode
            beforeNode = actualNode
            actualNode = actualNode.next
            counter = counter + 1

    def listSize(self):
        size_counter = 0
        start_node = self.head
        while start_node is not None:
            start_node = start_node.next
            size_counter = size_counter + 1
        return size_counter

    def printList(self):
        if self.head is None:
            print("Empty list")
        else:
            actual_node = self.head
            while True:
                if actual_node is None:
                    break
                else:
                    print(actual_node.data,"--->",actual_node.next)
                    actual_node = actual_node.next

list = linkedList()

list.insertNode("Kira")
list.insertNode("Milo")
list.insertNode("Merry")

list.insertNewHead("New Head")
list.insertBetween(3,"Between")
list.insertBetween(4,"NEw between")
list.printList()
print("Total of nodes:",list.listSize())
