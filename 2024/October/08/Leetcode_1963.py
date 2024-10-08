'''
    Leetcode Daily Question (08-10-2024)
    1963. Minimum Number of Swaps to Make the String Balanced
    Python3 solution
'''

class Solution:
    def minSwaps(self, s: str) -> int:
        st = []
        for i in s:
            if i == '[':
                st.append(i)
            else:
                if st:
                    if st[-1] == '[':
                        st.pop()
                    else:
                        st.append(i)
                else:
                    st.append(i)
        # print(st)
        if not st:
            return 0
        return max(1, (len(st)+3)//4)