class Solution:
    def numTrees(self, n: int) -> int:
        uni_tree=[1]*(n+1)
        for nodes in range(2,n+1):
            total=0
            for root in range(1,nodes+1):
                total+=uni_tree[root-1] * uni_tree[nodes-root]
            uni_tree[nodes]=total
        return uni_tree[n]
