class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for index, number in enumerate(nums):
            diff = target - number 
            if diff in numbers and index!= numbers[diff]:
                return [min(numbers[diff], index), max(numbers[diff], index)]
            else:
                numbers[number] = index

        return []