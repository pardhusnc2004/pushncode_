'''
    GeeksforGeeks Daily Question (04-11-2024)
    Find All Triplets with Zero Sum
    Python3 solution
'''

class Solution:
    def findTriplets(self, arr):
        # Your code here
        d={}
        n=len(arr)
        temp=0
        for i in range(0,n):
            for j in range(i+1,n):
                temp=arr[i]+arr[j]
                if(temp in d):
                    d[temp].append([i,j])
                else:
                    d[temp]=[[i,j]]
        tpt=[]
        vis={}
        ans=[]
        for i in range(n):
            temp=-arr[i]
            if(temp in d):
                for a,b in d[temp]:
                    tpt=sorted([i,a,b])
                    if(i!=a and i!=b and (tuple(tpt) not in vis)):
                        ans.append(tpt)
                        vis[tuple(tpt)]=1
        return ans