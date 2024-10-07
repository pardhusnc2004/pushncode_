'''
    Leetcode Daily Question (07-10-2024)
    2696. Minimum String Length After Removing Substrings
    Python3 solution
'''

class Solution:
    def minLength(self, s: str) -> int:
        st = []
        for i in s:
            if not st or i not in ['B', 'D']:
                st.append(i)
            else:
                if i == 'B' and st[-1] == 'A':
                    st.pop()
                elif i == 'D' and st[-1] == 'C':
                    st.pop()
                else:
                    st.append(i)
        return len(st)