from typing import List
from collections import Counter, defaultdict


# Given an integer array nums, return true if any value 
# appears more than once in the array, otherwise return false.
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:    
        
        dubs = {}
        for i, num in enumerate(nums):
            if num not in dubs:
                dubs[num]  = num
            else: 
                return True
        return False

    """
    Given two strings s and t, return true if the two strings are anagrams of each other, 
    otherwise return false. An anagram is a string that contains the exact same characters as another string,
    but the order of the characters can be different.
    """
    def isAnagram(self, s: str, t: str) -> bool:
        slen = Counter(s) 
        tlen = Counter(t) 
        return slen == tlen

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
            
        for i, num in enumerate(nums):
            counter_val =  target - num
            
            if counter_val in dic: 
                
                return [dic[counter_val], i]

            dic[num] = i                
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        nlbi = []
        angrams = defaultdict(list)
        for str in strs:
            count = [0]*26
            
            for c in str: 
                count[ord(c) - ord("a")] += 1
                
                
            angrams[tuple(count)].append(str)
            
        return angrams.values()
                
                
                
            
            
            
            
        
sol = Solution()
hasduplicate = sol.hasDuplicate(nums = [1,2,3,3])
isAnagram_1 = sol.isAnagram("racecar","carrace")
isAnagram_2 = sol.isAnagram("jam","car")
twoSum_1 = sol.twoSum(nums = [3,4,5,6], target = 7)
groupAnagram = sol.groupAnagrams(strs = ["act","pots","tops","cat","stop","hat"])
print(groupAnagram)