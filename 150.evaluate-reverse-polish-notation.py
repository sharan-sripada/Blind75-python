#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack= []
        op = ["+", "-", "/","*"]
        for s in tokens:
            if s not in op:
                stack.append(int(s))
            else:
                if s == "*":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a*b)
                if s == "/":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(float(b)/a))
                if s == "+":
                    stack.append(stack.pop()+stack.pop())
                if s == "-":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b-a)
        
        return stack.pop()

        
# @lc code=end

