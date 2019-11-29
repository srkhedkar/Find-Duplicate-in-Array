class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        normal_set = set()

        for i in A:
            if i in normal_set:
                return i
            else:
                normal_set.add(i)
        
        return -1
