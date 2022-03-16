from typing import List


class Solution:

    def __init__(self, list, target):

        self.list = list
        self.target = target

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

    def twoSumDict(self, nums: List[int], target: int) -> List[int]:

        hash_map = {}
        for i in range(len(nums)):
            hash_map[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_map and complement != nums[i]:
                return [i, hash_map[complement]]

    def twoSumOne(self, nums: List[int], target: int) -> List[int]:

        hash_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in hash_map and complement != nums[i]:
                return [i, hash_map[complement]]

            hash_map[nums[i]] = i


list = [4, 5, 7, 9, 11]
target = 20
sol1 = Solution(list, target)
answer = sol1.twoSum(list, target)
hash_ans = sol1.twoSumDict(list, target)
one_pass = sol1.twoSumOne(list, target)

print(answer)
print(hash_ans)
print(one_pass)
