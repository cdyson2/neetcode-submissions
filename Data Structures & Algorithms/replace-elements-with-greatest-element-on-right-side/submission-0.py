class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        rightMax = -1

        for i in range(len(arr)):
            rightMax = -1
            for j in range(i+1, len(arr)):
                maxElement = max(arr[j], rightMax)
                rightMax = maxElement
            arr[i] = rightMax
        return arr

