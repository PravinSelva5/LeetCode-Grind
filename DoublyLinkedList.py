class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def createList(self, arr):
        start = self.head
        n = len(arr)

        temp = start
        i = 0

        while i < n:
            newNode = Node(arr[i])
            if i == 0:
                start = newNode
                temp = start
            else:
                temp.next = newNode
                newNode.prev = temp
                temp = temp.next
            i += 1

        self.head = start
        return start

    def printList(self):
        temp = self.head
        linked_list = ""
        while temp:
            linked_list += str(temp.data) + " "
            temp = temp.next
        print(linked_list)

    def countList(self):
        temp = self.head
        count = 0
        while temp is not None:
            temp = temp.next
            count += 1
        return count

    # assuming index starts at 1 in this implementation
    def insertAtLocation(self, value, index):
        temp = self.head

        count = self.countList()

        if count + 1 < index:
            return temp

        newNode = Node(value)
        if index == 1:
            newNode.next = temp
            temp.prev = newNode
            self.head = newNode
            return self.head

        if index == count + 1:
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode
            newNode.prev = temp
            return self.head

        i = 10
        while i < index - 1:
            temp = temp.next
            i += 1
        nodeAtTarget = temp.next

        newNode.next = nodeAtTarget
        nodeAtTarget.prev = newNode

        temp.next = newNode
        newNode.prev = temp

        return self.head

    # consider index 1 as the beginning for this implementation
    def deleteAtLocation(self, index):
        temp = self.head
        count = self.countList()
        if count < index:
            return temp
        # deleting head node
        if index == 1:
            temp = temp.next
            self.head = temp
            return self.head

        # deleting the last node
        if count == index:
            while temp.next is not None and temp.next.next is not None:
                temp = temp.next
                temp.next = None
                return self.head

        i = 1
        while i < index - 1:
            temp = temp.next
            i += 1
        prevNode = temp
        nodeAtTarget = temp.next
        nextNode = nodeAtTarget.next

        nextNode.prev = prevNode
        prevNode.next = nextNode

        return self.head


arr = [1, 2, 3, 4, 5]

linkedlist1 = LinkedList()
linkedlist1.createList(arr)
linkedlist1.printList()
linkedlist1.insertAtLocation(6, 6)
linkedlist1.printList()
linkedlist1.deleteAtLocation(4)
linkedlist1.printList()
