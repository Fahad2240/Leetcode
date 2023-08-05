class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(nums, low, mid, high):
            temp = []  # temporary array
            left = low  # starting index of left half of arr
            right = mid + 1  # starting index of right half of arr

            # storing elements in the temporary array in a sorted manner
            while left <= mid and right <= high:
                if nums[left] <=nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1

            # if elements on the left half are still left
            while left <= mid:
                temp.append(nums[left])
                left += 1

            # if elements on the right half are still left
            while right <= high:
                temp.append(nums[right])
                right += 1

            # transferring all elements from temporary to arr
            for i in range(low, high + 1):
                nums[i] = temp[i - low]
                
        def countPairs(arr, low, mid, high):
            right = mid + 1
            cnt = 0
            for i in range(low, mid + 1):
                while right <= high and arr[i] > 2 * arr[right]:
                    right += 1
                cnt += (right - (mid + 1))
            return cnt
        
        def mergeSort(nums, low, high):
            cnt = 0
            if low >= high:
                return cnt
            mid = (low + high) // 2
            cnt += mergeSort(nums, low, mid)  # left half
            cnt += mergeSort(nums, mid + 1, high)  # right half
            cnt += countPairs(nums, low, mid, high)  # Modification
            merge(nums, low, mid, high)  # merging sorted halves
            return cnt
        
        return mergeSort(nums,0,len(nums)-1)
                # MergeSort in Python

