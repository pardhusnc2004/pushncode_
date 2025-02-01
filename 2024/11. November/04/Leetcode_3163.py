'''
    Leetcode Daily Question (04-11-2024)
    3163. String Compression III
    Python3 solution
'''

class Solution:
    def compressedString(self, word: str) -> str:
        st = [[-1, '-']]
        for letter in word:
            if letter == st[-1][1]:
                if st[-1][0] == 9:
                    st.append([1, letter])
                else:
                    st[-1][0] += 1
            else:
                st.append([1, letter])
        comp = ""
        for i in st[1:]:
            comp += str(i[0])+i[1]
        return comp