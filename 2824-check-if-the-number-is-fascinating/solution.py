class Solution:
    def isFascinating(self, n: int) -> bool:
        s=str(n)+str(n*2)+str(n*3)
        if ''.join(sorted(s))=="123456789":
            return True
        else:
            return False
