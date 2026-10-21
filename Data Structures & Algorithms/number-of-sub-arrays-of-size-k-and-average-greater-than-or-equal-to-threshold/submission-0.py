class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        L = 0
        tot = 0

        for R in range(len(arr)):
            if R-L+1 > k:
                tot-=arr[L]
                L+=1
            
            tot+=arr[R]
            avg=tot/k

            if R-L+1 == k and avg >= threshold:
                count+=1
        
        return count
                


        