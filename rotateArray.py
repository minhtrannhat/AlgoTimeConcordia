class Solution:
    
            
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        
        def reverse(arr: List[int], start: int, end: int):
            while(start < end):
                temp = arr[start]
                arr[start] = arr[end]
                arr[end] = temp
                start+=1
                end-=1
            
            
        k %= len(nums)
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)
