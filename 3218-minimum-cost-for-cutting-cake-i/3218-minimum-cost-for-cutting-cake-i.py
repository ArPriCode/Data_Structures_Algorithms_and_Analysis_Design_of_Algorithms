class Solution(object):
    def minimumCost(self, m, n, horizontalCut, verticalCut):
        def cal(l1, m, l2, n, h, v):
              if not h and not v:
                return 0
              p = -1
              m = 0
              typ = None
              for i in range(len(h)):
                if m<h[i]:
                    m = h[i]
                    p = i
                    typ= 1
              for i in range(len(v)):
                if m<v[i]:
                    m = v[i]
                    p = i
                    typ=0
              if typ ==0:
                 return m + cal(l1, m, l2, p+1, h, v[:p])+ cal(l1, m, p+1, n, h, v[p+1:])
              else:
                 return m + cal(l1, p+1, l2, n, h[:p], v)+ cal(p+1, m, l2, n, h[p+1:], v)
        return cal(0, m, 0, n, horizontalCut, verticalCut)