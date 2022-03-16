class Stack(object):

    def __init__(self):
        self.items = []

    def push(self, value: int):
        self.items.append(value)

    def pop(self):
        self.items.pop()

    def peek(self):
        if self.items is None:
            return self.items[-1]
        else:
            None
    def size(self):
        if self.items is not None:
            return len(self.items)
        else:
            return None
    def isEmpty(self):

        if not self.items:
            return print("Stack is empty!")
        else:
            return print("Stack is not empty!")
    def show(self):

        for i in self.items:
            print(i, end=" ")

stk = Stack()
stk.push(3)
stk.push(2)
stk.push(8)
stk.push(4)
stk.show()
stk.pop()
print()
stk.show()








