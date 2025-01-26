from create import Node, LinkedList

if __name__ == '__main__':
    list = LinkedList()

    list.head = Node(1)
    second = Node(2)
    third = Node(3)

    list.head.next = second
    second.next = third

    list.printList()