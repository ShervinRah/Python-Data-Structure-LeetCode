class Balanced:

    def __init__(self):
        self.pattern = pattern

    def isBalanced(self, pattern: str) -> bool:

        length= len(self.pattern)

        if length % 2 != 0:
            return False
        stack = []

        for i in pattern:
            #split_to_char = []
            if i == '[' or i == '{' or i == '(':
                stack.append(i)

            if i == ']' or i == '}' or i == ')':

                char = stack.pop()
                if (char == '[' and i != ']') or (char == '(' and i != ')') or (
                        char == '{' and i != '}'):
                    return False

        return True






pattern = "([({})])"
result = Balanced()
isTrue = result.isBalanced(pattern)
print(isTrue)

