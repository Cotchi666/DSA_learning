
class Solution:
    # Method to find median
    def MedianOfArrays(self, arr1, arr2):
        n = len(arr1)  #[1, 4, 7 ]             = 2 
        m = len(arr2)  #[2, 3, 5, 6 ]          = 3 
                       #[1, 2, 3, 4, 5, 6, 7]  = 6 
        if (n > m):
            return self.Median(arr2, arr1)  # Swapping to make A smaller
        start = 0
        end   = n 
        while (start <= end):
            midA =  (start + end) // 2        # 1
            midB = (n + m + 1) // 2 - midA    # 2
            # checking overflow of indices
            leftA  = arr1[midA - 1] if (midA > 0) else float('-inf')
            leftB  = arr2[midB - 1] if (midB > 0) else float('-inf')
            rightA = arr1[midA] if (midA < n) else float('inf')
            rightB = arr2[midB] if (midB < m) else float('inf')
            print("midA", midA)
            print("midB",midB)
            print("left A", leftA)
            print("left b", leftB)
            print("rightA", rightA)
            print("rightB", rightB)
            # if correct partition is done
            if leftA <= rightB and leftB <= rightA:
                if ((m + n) % 2 == 0):
                    print("max1", max(leftA,leftB))
                    print("max1", leftA)
                    print("max1", leftB)

                    return (max(leftA, leftB) + min(rightA, rightB)) / 2.0
                print("max", max(leftA,leftB))
                print("max", leftA)
                print("max", leftB)

                return max(leftA, leftB)

            elif (leftA > rightB):
                print("max3", max(leftA,leftB))
                print("max3", leftA)
                print("max3", leftB)

                end   = midA - 1
            else:
                print("max4", max(leftA,leftB))
                print("max4", leftA)
                print("max4", leftB)

                start = midA + 1

# Driver code
ans = Solution()
# arr1 = [-5, 3, 6, 12, 15]
# arr2 = [-12, -10, -6, -3, 4, 10]
arr1 = [1, 4, 7 ]
arr2 = [2, 3, 5, 6 ]   
print("Median of the two arrays is {}".format(ans.MedianOfArrays(arr1, arr2)))

# This code is contributed by Arpan
#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        m = input()
        arr1=[int(x) for x in input().split()]
        n = input()
        arr2=[int(x) for x in input().split()]
        
        
        ob = Solution()
        print(ob.MedianOfArrays(arr1,arr2))

# } Driver Code Ends