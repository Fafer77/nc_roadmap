from sortedcontainers import SortedList
from typing import List

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        parent = list(range(c + 1))
        size = [1] * (c + 1)
        online_map = {}
        is_online = [True] * (c + 1)
        res = []

        # build DSU using connections
        for x, y in connections:
            self.union(x, y, parent, size)
        
        for v in range(1, c + 1):
            representative = self.find(v, parent)
            if representative not in online_map:
                online_map[representative] = SortedList()
            online_map[representative].add(v)
        
        # process queries
        for s, x in queries:
            if s == 1:
                if is_online[x]:
                    res.append(x)
                else:
                    r = self.find(x, parent)
                    if not online_map[r]:
                        res.append(-1)
                    else:
                        lowest = online_map[r][0]
                        res.append(lowest)
            else:
                r = self.find(x, parent)
                if x in online_map[r]:
                    online_map[r].remove(x)
                    is_online[x] = False

        return res

    def union(self, i, j, parent, size):
        pi = self.find(i, parent)
        pj = self.find(j, parent)

        if pi == pj:
            return
        
        if size[pi] < size[pj]:
            pi, pj = pj, pi
        parent[pj] = pi
        size[pi] += size[pj]
    
    def find(self, i, parent):
        if parent[i] != i:
            parent[i] = self.find(parent[i], parent)
        
        return parent[i]

