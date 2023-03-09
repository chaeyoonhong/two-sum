def twoSum(nums, target) -> list[int]:
	 for num1 in nums:
                for num2 in nums:
                        if num1+num2 == target:
                               return [num1,num2]

