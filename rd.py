from typing import List
from collections import Counter


class Solution:
	def plusOne(self, digits) :
	
		x = int("".join(map(str, digits)))
		x += 1
		return list(map(int, str(x)))
			
	def isPalindrome(self, s: str) -> bool:
		
		left = 0
		ls = list("".join(s).strip())
		right = len(ls)
		print(ls)
				
	def repeatedNTimes(self, nums):
		dic = {}
		
		for num in nums:
			if num in dic:
				return num
			
			else:
				dic[num] = 1
			
	
			
		

	def threeSum(self, nums: List[int]) -> List[List[int]]:		
		pass

        
if __name__ == "__main__":
    sol = Solution()
    nums_1 = [3,2,3,2,2,2]
    nums_2 = [1,2,3,4]

    print(sol.divideArray(nums_1))
    print(sol.divideArray(nums_2))

    nums_min = [0,1,1,1,0,0]
    nums_min_2 =  [0,1,1,1]

    assert sol.minOperations(nums_min) == 3
    assert sol.minOperations(nums_min) == -1
    



