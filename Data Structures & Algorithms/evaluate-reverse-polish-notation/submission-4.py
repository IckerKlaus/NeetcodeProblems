class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in {"+", "-", "*", "/"}:
                stack.append(int(t))
                continue
            val_2 = stack.pop()
            val_1 = stack.pop()
            if t == "+":
                stack.append(val_1 + val_2)
            elif t == "-":
                stack.append(val_1 - val_2)
            elif t == "*":
                stack.append(val_1 * val_2)
            elif t == "/":
                stack.append(int(val_1 / val_2))
        return stack[0]