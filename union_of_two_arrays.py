class Solution:    
    def findUnion(self, a, b):
        return list(set(sorted(a) + sorted(b)))