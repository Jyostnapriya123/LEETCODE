class Solution:
    def reverseWords(self, s: str) -> str:
       
    
        result=[]
        l1=s.split()
        for word in l1:
            result.append(word[::-1])
        return " ".join(result)
