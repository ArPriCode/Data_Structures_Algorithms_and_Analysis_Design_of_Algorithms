class Solution(object):
    def minFlips(self, g):
        z1=0
        z2=0
        for i in g:
            l=0
            r=len(i)-1
            c=0
            while l<r:
                if i[l]!=i[r]:
                    c=c+1
                l=l+1
                r=r-1
            z1=z1+c
        k=[]
        for i in range(len(g[0])):
            p=[]
            for j in range(len(g)):
                p.append(g[j][i])
            k.append(p)
        for i in k:
            c=0
            l=0
            r=len(i)-1
            while l<r:
                if i[l]!=i[r]:
                    c=c+1
                l=l+1
                r=r-1
            z2=z2+c
        return min(z1,z2)        