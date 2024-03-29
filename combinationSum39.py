"""
39. Combination Sum: https://leetcode.com/problems/combination-sum/description/   Amazon question. 

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. 
The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.
The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
"""


# Correct solution beats 6% runtime 74% memory:
class Solution(object):
    def combinationSum(self, candidates, target):  
        ans = []
        for c in candidates:
            if c == target:
                ans.append([c]) 
                candidates.remove(c) # no point in checking this num over and over later

        def search(cur, cur_sum):
            if cur_sum == target:
                cur.sort()
                if cur not in ans:
                    ans.append(cur)
            elif cur_sum > target:
                return
            for i in range(len(candidates)):
                L = cur + [candidates[i]]
                # print(L)
                search(L, cur_sum+candidates[i])
        search([],0)
        return ans 



# First draft passes 27 / 160 testcases:
class Solution(object):
    def combinationSum(self, candidates, target):        
        ans = []
        comboList=[]
        for c in candidates:
            if c == target:
                ans.append([target])
            else: 
                comboList.append([c])
        print(comboList)

        for num in candidates:
            tempList=[]
            for lst in comboList:
                lst.append(num)
                total = sum(lst)
                if total < target:
                    tempList.append(lst)
                elif total==target:
                    if lst not in ans:
                        lst.sort()
                        ans.append(lst)
                else:
                    pass
            comboList=tempList
        return ans
