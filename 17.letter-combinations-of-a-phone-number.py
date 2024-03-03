#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        def backtrack(digits, index,res,list):
            if index == len(digits):
                res.append(list)
                return
            string = phone[digits[index]]
            
            for s in string:
                backtrack(digits,index+1,res,list+s)
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        backtrack(digits,0,result,"")

        
        
                
        return result
                
    
    
        
# @lc code=end

