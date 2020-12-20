#Suppose an array sorted in ascending order is rotated at some pivot unknown to
# you beforehand. Find the minimum element in O(log N) time. You may assume the #array does not contain duplicates.

#For example, given [5, 7, 10, 3, 4], return 3.

def helper(arr,high,low):
    print("test")

if __name__ == "__main__":
    A = [5, 7, 10, 3, 4]
    low, high = 0, len(A)-1
    helper(A, high, low)
