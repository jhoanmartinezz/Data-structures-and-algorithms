class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def insertNode(self, newData):
        new_node = Node(newData)
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

    def insertHead(self, dataHead):
        node_head = Node(dataHead)
        temp_node = self.head
        self.head = node_head
        node_head.next = temp_node
        del temp_node

    def insertBetween(self, posicion, btwData):
        between_node = Node(btwData)
        actual_posicion = 0
        current_node = self.head
        while current_node is not None:
            if posicion == actual_posicion:
                beforeNode.next = between_node
                between_node.next = current_node
            beforeNode = current_node
            current_node = current_node.next
            actual_posicion += 1

    def printList(self):
        if self.head is None:
            print("Empty list")
        else:
            actual_node = self.head
            while True:
                if actual_node is None:
                    break
                else:
                    print(actual_node.data," ---> next address --->",actual_node.next)
                    actual_node = actual_node.next

list = linkedList()

list.insertNode("Kira")
list.insertNode("Milo")
list.insertNode("Merry")
list.insertNode("FER")
list.printList()
print("*"*80)
#list.insertHead("First")
btw = Node("Between")
list.insertBetween(1,"Between Node")
list.printList()
