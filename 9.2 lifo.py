'#ctrl + z'
'#browser navigation'
'#-----------time complexity O(1)-----------'
'#-----------space complexity O(n)-----------'
'#sotre n elements in the list'

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class StackLifo:
    def __init__(self):
        self.head = None
        self.size = 0
    #push operation or add elements "add node"
    def push(self, dataNode):
        new_node = Node(dataNode)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
    #pop operation always delete the last node inserted "delete head node"
    def pop(self):
        if self.head is not None:
            data = self.head.data
            self.size -= 1
            if self.head.next is not None:
                self.head = self.head.next
            else:
                self.head = None
            return data
        else:
            return None
    #peek brig the top element without deleting it
    def peek(self):
        if self.head is not None:
            return self.head.data
        else:
            return None
    #traverse the list to check elements
    def traverseStack(self):
        if self.head is None:
            print("Empty stack")
        else:
            current_head = self.head
            while current_head is not None:
                print(current_head.data,"--->",current_head.next)
                current_head = current_head.next

turno = StackLifo()
turno.push("1.Kira")
turno.push("2.milo")
turno.push("3.merry")
turno.push("4.molly")
turno.traverseStack()
print("*"*80)
#print(turno.pop())
print("*"*80)
#turno.traverseStack()
