'''
    GeeksforGeeks Daily Question (21-02-2025)
    Parenthesis Checker
    Python3 solution
'''

class Solution:
    def isBalanced(self, s):
        # code here
        st = []
        for i in s:
            if i in "[({":
                if i == '[':
                    st.append(']')
                if i == '{':
                    st.append('}')
                if i == '(':
                    st.append(')')
            else:
                if not st or st[-1] != i:
                    return False
                st.pop()
        return not st