class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mac = -1
        
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = mac
            mac = mac if mac > temp else temp
            
        return arr