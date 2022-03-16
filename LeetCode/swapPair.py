class swapNodes:

    def __init__(self, value = 0, next = None):

        self.value = value
        self.next = next


    def swapPairNodes(self, list):

        dummy_head = swapNodes(0, list)
        prev = dummy_head
        curr = list

        while curr and curr.next:

            next_pair = curr.next.next
            second = curr.next

            second.next = curr
            curr.next = next_pair
            prev.next = second

            prev = curr
            curr = next_pair

        return dummy_head.next

    def printSwap(self, list):

        lst = swapNodes(list)
        result = lst.swapPairNodes(list)

        while result.next is not None:
            print(result.value, " -> ", end="")
            result = result.next

        print(result.value)

    def show(self,list):
        lst = list
        while lst.next is not None:
            print(lst.value," -> ", end ="")
            lst = lst.next

        print(lst.value)






list = swapNodes(1)
list.next = swapNodes(2)
list.next.next = swapNodes(3)
list.next.next.next = swapNodes(4)

list.show(list)
list.printSwap(list)



