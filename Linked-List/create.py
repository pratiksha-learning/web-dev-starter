# create a node 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


#  create a link list class
class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end="->")
            temp = temp.next

if __name__ == '__main__':

    list = LinkedList()

    list.head = Node(1)
    second = Node(2)
    third = Node(3)

    # print(list.head) -> prints address of the variable

    list.head.next = second
    second.next = third
