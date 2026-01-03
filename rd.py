from typing import List
from collections import Counter


class Solution:
	
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		
		i = 0
		j = 1 
		k = len(nums)-1
		
		nums = sorted(nums)
		print(nums)
		list_of_triplets = []
		while i < k:
			diff = nums[i] + nums[k]
			
			while j < k:
				print(i,j,k)
				if diff + nums[j] == 0:
					list_of_triplets.append([nums[i], nums[j], nums[k]])
					k -= 1
					break
				j += 1
					
			
			j = + 1
			i += 1
			
			if i > 0 and nums[i] == nums[i-1]:
				
				print("Hier")
				continue
		return list_of_triplets

	

	def threeSum_wrong(self, nums: List[int]) -> List[List[int]]:
		sort = sorted(nums)
		left,mid, right = 0, 1, 2 
		list_of_trips = []
		if len(nums) == 0:
			return []

		while right < len(nums):
			l_pointer,m_pointer, r_pointer = sort[left], sort[mid], sort[right]

			while right < len(sort):
				r_pointer =  sort[right]
				if l_pointer + m_pointer + r_pointer == 0:
					list_of_trips.append([l_pointer, m_pointer, r_pointer])
				right += 1
			left += 1
			mid += 1
			right = mid + 1
		return list_of_trips

			
	def plusOne(self, digits):
	
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
			
	


if __name__ == "__main__":
	sol = Solution()
	nums_3sum = [-1,0,1,2,-1,-4]
	nums_3sum2 = [0,0,0,0]
	print(sol.threeSum(nums_3sum2))





