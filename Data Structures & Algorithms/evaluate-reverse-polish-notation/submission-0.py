class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for c in tokens:
            if c not in {'+','-','/','*'}:
                stack.append(int(c))
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                match c:
                    case '+':
                        res = n1+n2
                    case '-':
                        res = n1-n2
                    case '*':
                        res = n1*n2
                    case '/':
                        res = int(n1/n2)
                stack.append(res)
        return stack[-1]
