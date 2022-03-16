class ListNode:
    def __init__(self, value=0 , next = None):
        self.value = value
        self.next = next

    def addTwoNums(self, lst1, lst2):
        dummy_head = ListNode()
        list1 = lst1
        list2 = lst2
        result = dummy_head
        carry = 0

        while list1 is not None or list2 is not None:
            x = 0
            y = 0

            if list1 is not None:
                x = list1.value
            else:
                x = 0
            if list2 is not None:
                y = list2.value
            else:
                y = 0

            sum = x + y + carry
            carry = int(sum / 10)
            result.next = ListNode(sum % 10)
            result = result.next

            if list1 is not None:
                list1 = list1.next
            if list2 is not None:
                list2 = list2.next

        if carry > 0:
            result.next = ListNode(carry)
        return dummy_head.next

    def show(self,list):
        lst = list
        while lst.next is not None:
            print(lst.value," -> ", end ="")
            lst = lst.next

        print(lst.value)

    def showSum(self,lst1, lst2):
        lst = ListNode(lst1,lst2)
        result = lst.addTwoNums(lst1,lst2)

        while result.next is not None:
            print(result.value," -> ", end ="")
            result = result.next

        print(result.value)


list1 = ListNode(3)
list1.next = ListNode(2)
list1.next.next = ListNode(1)
list1.show(list1)

list2 = ListNode(6)
list2.next = ListNode(5)
list2.next.next = ListNode(3)
list2.show(list2)
solution = ListNode()
solution.showSum(list1,list2)






