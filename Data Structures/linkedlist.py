class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = next

class LinkedList:

    def __init__(self):
      self.head = None
        #hello

    def append(self, value):

      new_node = Node()
      new_node.value = value
      new_node.next = None
      if self.head is None:
          self.head = new_node
      else:
        tmp = self.head
        while tmp.next is not None:
            tmp = tmp.next
        tmp.next = new_node

    def show(self):
        start = self.head
        while start.next is not None:
            print(start.value," -> ",end="")
            start = start.next
        print(start.value)


linked_list = LinkedList()
linked_list.append(4)
linked_list.append(3)
linked_list.append(8)
linked_list.append(2)
linked_list.append(9)
linked_list.show()








