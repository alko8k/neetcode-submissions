class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        toDo = []
        check = {"+", "-", "*", "/"}
        for s in tokens: 
            if s not in check:
                toDo.append(int(s))
            elif s == "+":
                first = toDo.pop()
                second = toDo.pop()
                toDo.append(first + second)
            elif s == "*":
                first = toDo.pop()
                second = toDo.pop()
                toDo.append(first * second)
            elif s == "-":
                first = toDo.pop()
                second = toDo.pop()
                toDo.append(second - first)
            elif s == "/":
                first = toDo.pop()
                second = toDo.pop()
                toDo.append(int(second / first))
        return toDo.pop()

            