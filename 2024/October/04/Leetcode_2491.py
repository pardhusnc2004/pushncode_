'''
    Leetcode Daily Question (04-10-2024)
    2491. Divide Players Into Teams of Equal Skill
    Python3 solution
'''

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        s = set()
        # print(skill)
        res = 0
        i, j = 0, len(skill)-1
        while i<j:
            s.add(skill[i]+skill[j])
            res += skill[i]*skill[j]
            i += 1
            j -= 1
            if len(s) > 1:
                return -1
        return res if len(s) == 1 else -1