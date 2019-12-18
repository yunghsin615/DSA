
# coding: utf-8

# In[1]:


from collections import defaultdict 

class Graph:
    def __init__(self):
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def BFS(self, s): 
        queue = []
        res = []
        for j in range(len(self.graph)-1):
            for i in range(0,len(self.graph[s])):
                if self.graph[s][i] not in queue and self.graph[s][i] not in res:
                    queue.append(self.graph[s][i])
            res.append(s)
            s = queue[j]
        res.append(s)
        return res
    
    def DFS(self, s):
        stack = []
        res = []
        for j in range(len(self.graph)-1):
            for i in range(0,len(self.graph[s])):
                if self.graph[s][i] not in stack and self.graph[s][i] not in res:
                    stack.append(self.graph[s][i])
            if len(res) == 0:
                res.append(s)
            s = stack.pop(-1)
            res.append(s)
        return res


# 參考資料：
# 
# https://docs.google.com/presentation/d/e/2PACX-1vSYJYXUXvGAeTZ5fknxj_-EPm3zxgy4ITdImrXzy63Y-iZgs8uwVNmOaZlnx9fUNzsbo8kphvMTa0c4/pub?start=false&loop=false&delayms=3000&slide=id.p
# 
# http://f74461036.pixnet.net/blog/post/352335176
# 
# https://docs.google.com/presentation/d/e/2PACX-1vTma_vOZyE70O23KWw4I4Y78aAaT5fJSTq7Mae912kCwka_u5ZMWPoo14D86-x-57kZPbb6hAGktSW4/pub?start=false&loop=false&delayms=3000&slide=id.p
# 
# http://isee.scu.edu.tw/mod/url/view.php?id=549964
# 
# https://blog.csdn.net/deqiangxiaozi/article/details/75808863
