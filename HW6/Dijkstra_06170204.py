
# coding: utf-8

# In[ ]:


from collections import defaultdict 
import math

class Graph(): 
    
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        
    def addEdge(self,u,v,w): 
        self.graph.append([w,u,v])
        
    def Dijkstra(self, s): 
        dis = [float("inf")] * self.V
        com = [float("inf")] * self.V
        dis[0] = 0
        
        for i in range(len(g.graph[s])):
            if g.graph[s][i] > 0:
                dis[i] = g.graph[s][i]
                com[i] = g.graph[s][i]
                
        while com != [float("inf")] * self.V:
            s = com.index(min(com))
            com[s] = float("inf")
            for j in range(len(g.graph[s])):
                if g.graph[s][j] == 0:
                    continue
                elif dis[s] + g.graph[s][j] < dis[j]:
                    dis[j] = dis[s] + g.graph[s][j]
                    com[j] = dis[s] + g.graph[s][j]
                    
        dict = {}
        for k in range (self.V):
            dict[str(k)] = dis[k]
            
        return dict
    
    def Kruskal(self):
        g.graph.sort()
        root = [-1] * self.V
        res = []
        dict = {}
        
        for i in range(0,len(g.graph)):
            if root[g.graph[i][1]] == root[g.graph[i][2]]:
                if root[g.graph[i][1]] == -1 and root[g.graph[i][2]] == -1:
                    root[g.graph[i][1]] = g.graph[i][1]
                    root[g.graph[i][2]] = g.graph[i][1]
                    res.append(g.graph[i][0])
                else:
                    continue
            else:
                if root[g.graph[i][1]] == -1:
                    root[g.graph[i][1]] = g.graph[i][1]
                    j = 0
                    temp = root[g.graph[i][2]]
                    while j < len(root):
                        if root[j] == temp:
                            root[j] = g.graph[i][1]
                        j += 1
                elif root[g.graph[i][2]] == -1:
                    root[g.graph[i][2]] = root[g.graph[i][1]]
                else:
                    temp1 = root[g.graph[i][2]]
                    for k in range(0,len(root)):
                        if root[k] == temp1:
                            root[k] = root[g.graph[i][1]]
                res.append(g.graph[i][0])
                
            h = str(g.graph[i][1]) + '-' + str(g.graph[i][2])
            dict[h] = res[-1]
        
        return dict


# 參考資料
# 
# https://docs.google.com/presentation/d/e/2PACX-1vTgHO5AkHJS6iN6bnnBMMdHv6E4rabnrC0KwyTRfjad8Ab3IQjbnGvZuQOjDC9t7nKqeroiwcuasJrI/pub?start=false&loop=false&delayms=3000&slide=id.p
# https://ithelp.ithome.com.tw/articles/10209593
# https://segmentfault.com/a/1190000011908915
# https://blog.csdn.net/fengjiexyb/article/details/77435676
# https://www.jianshu.com/p/fbf71e6da515
# https://docs.google.com/presentation/d/e/2PACX-1vTorNDEyhYA4ZAt5jEqOmFs2cQiUAYvkTp-R0DOn9B3c1MuUecV-a1wNakFIrJxA6AoUFGzbl3OQBIJ/pub?start=false&loop=false&delayms=3000&slide=id.p
# https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
