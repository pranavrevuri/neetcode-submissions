class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        int_1, int_2 = 0, 0


        for i in range(len(tokens)):
            if tokens[i] not in "+-/*":
                stack.append(int(tokens[i]))
            else:
                int_1 = stack.pop()
                int_2 = stack.pop()

                if tokens[i] == "+":
                    stack.append(int_1+int_2)
                elif tokens[i] == "-":
                    stack.append(int_2-int_1)
                elif tokens[i] == "*":
                    stack.append(int_1*int_2)
                elif tokens[i] == "/" and int_1 != 0:
                    stack.append(int(int_2/int_1))
        
        return stack[0]