
# coding: utf-8

# In[1]:


class TreeNode(object):

    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    
    def insert(self,root,val):
        if val <= root.val:
            if root.left == None:
                root.left = TreeNode(val)
                return root.left
            else:
                p = root.left
                return self.insert(p,val)
        else:
            if root.right == None:
                root.right = TreeNode(val)
                return root.right
            else:
                p = root.right
                return self.insert(p,val)

    def search(self,root,target):
        if target < root.val:
            if root.left == None:
                return None
            else:
                p = root.left 
                return self.search(p,target)
        elif target > root.val:
            if root.right == None:
                return None
            else:
                p = root.right
                return self.search(p,target)
        else:
            return root

    def delete(self,root,target):
        i = root
        parent = root
        while target != root.val: #找parent、x
            parent = root
            if target < root.val:
                if root.left == None:
                    break
                else:
                    root = root.left 
            elif target > root.val:
                if root.right == None:
                    break
                else:
                    root = root.right
                    
        if target == root.val:
            if root.left == None and root.right == None: #target沒有孩子
                if parent.val < root.val:
                    parent.right = None
                elif parent.val > root.val:
                    parent.left = None
                else:
                    del root.val
            elif root.left == None and root.right != None: #target沒有左孩子 有右孩子
                if parent.val < root.val:
                    parent.right = root.right
                elif parent.val > root.val:
                    parent.left = root.right
                else:
                    parent = root
                    root = root.right
                    if root.left == None and root.right == None: #target.right沒有孩子
                        parent.val = root.val
                        parent.right = None
                    elif root.left == None and root.right != None: #target.right沒有左孩子 有右孩子
                        parent.val = root.val
                        parent.right = root.right
                    elif root.left != None and root.right == None: #target.right有左孩子 沒有右孩子
                        temp = root
                        while temp.left != None:
                            Minparent = temp
                            temp = Minparent.left

                        Min = temp
                        parent.val = Min.val
                        if Min.right != None:
                            Minparent.left = Min.right
                        else:
                            Minparent.left = None
                    else: #target.right有兩個孩子
                        temp = root
                        while temp.left != None:
                            Minparent = temp
                            temp = Minparent.left

                        Min = temp
                        parent.val = Min.val
                        if Min.right != None:
                            Minparent.left = Min.right
                        else:
                            Minparent.left = None
                        
                        
            elif root.left != None and root.right == None: #target有左孩子 沒有右孩子
                if parent.val < root.val:
                    parent.right = root.left
                elif parent.val > root.val:
                    parent.left = root.left
                else:
                    parent = root
                    root = root.left
                    if root.left == None and root.right == None: #target.left沒有孩子
                        parent.val = root.val
                        parent.left = None
                    elif root.left == None and root.right != None: #target.left沒有左孩子 有右孩子
                        temp = root
                        while temp.right != None:
                            Maxparent = temp
                            temp = Maxparent.right

                        Max = temp
                        parent.val = Max.val
                        if Max.left != None:
                            Minparent.right = Max.left
                        else:
                            Maxparent.right = None
                    elif root.left != None and root.right == None: #target.left有左孩子 沒有右孩子
                        parent.val = root.val
                        parent.left = root.left
                    else: #target.left有兩個孩子
                        temp = root
                        while temp.right != None:
                            Maxparent = temp
                            temp = Maxparent.right

                        Max = temp
                        parent.val = Max.val
                        if Max.left != None:
                            Maxparent.right = Max.left
                        else:
                            Maxparent.right = None
                            
            else: #target有兩個孩子
                temp = root.right
                if temp.left == None:
                    Minparent = root

                    Min = temp
                    root.val = Min.val
                    if Min.right != None:
                        Minparent.right = Min.right
                    else:
                        Minparent.right = None
                else:
                    while temp.left != None:
                        Minparent = temp
                        temp = Minparent.left

                    Min = temp
                    root.val = Min.val
                    if Min.right != None:
                        Minparent.left = Min.right
                    else:
                        Minparent.left = None
            self.delete(i,target)
        return i
        
    def modify(self,root,target,new_val):
        #self.delete(root,target)
        i = root
        while self.search(root,target) != None:
            parent = root
            while target != root.val: #找parent、x
                parent = root
                if target < root.val:
                    if root.left == None:
                        break
                    else:
                        root = root.left 
                elif target > root.val:
                    if root.right == None:
                        break
                    else:
                        root = root.right

            if target == root.val:
                if root.left == None and root.right == None: #target沒有孩子
                    if parent.val < root.val:
                        parent.right = None
                    elif parent.val > root.val:
                        parent.left = None
                    else:
                        del root.val
                elif root.left == None and root.right != None: #target沒有左孩子 有右孩子
                    if parent.val < root.val:
                        parent.right = root.right
                    elif parent.val > root.val:
                        parent.left = root.right
                    else:
                        parent = root
                        root = root.right
                        if root.left == None and root.right == None: #target.right沒有孩子
                            parent.val = root.val
                            parent.right = None
                        elif root.left == None and root.right != None: #target.right沒有左孩子 有右孩子
                            parent.val = root.val
                            parent.right = root.right
                        elif root.left != None and root.right == None: #target.right有左孩子 沒有右孩子
                            temp = root
                            while temp.left != None:
                                Minparent = temp
                                temp = Minparent.left

                            Min = temp
                            parent.val = Min.val
                            if Min.right != None:
                                Minparent.left = Min.right
                            else:
                                Minparent.left = None
                        else: #target.right有兩個孩子
                            temp = root
                            while temp.left != None:
                                Minparent = temp
                                temp = Minparent.left

                            Min = temp
                            parent.val = Min.val
                            if Min.right != None:
                                Minparent.left = Min.right
                            else:
                                Minparent.left = None


                elif root.left != None and root.right == None: #target有左孩子 沒有右孩子
                    if parent.val < root.val:
                        parent.right = root.left
                    elif parent.val > root.val:
                        parent.left = root.left
                    else:
                        parent = root
                        root = root.left
                        if root.left == None and root.right == None: #target.left沒有孩子
                            parent.val = root.val
                            parent.left = None
                        elif root.left == None and root.right != None: #target.left沒有左孩子 有右孩子
                            temp = root
                            while temp.right != None:
                                Maxparent = temp
                                temp = Maxparent.right

                            Max = temp
                            parent.val = Max.val
                            if Max.left != None:
                                Minparent.right = Max.left
                            else:
                                Maxparent.right = None
                        elif root.left != None and root.right == None: #target.left有左孩子 沒有右孩子
                            parent.val = root.val
                            parent.left = root.left
                        else: #target.left有兩個孩子
                            temp = root
                            while temp.right != None:
                                Maxparent = temp
                                temp = Maxparent.right

                            Max = temp
                            parent.val = Max.val
                            if Max.left != None:
                                Maxparent.right = Max.left
                            else:
                                Maxparent.right = None

                else: #target有兩個孩子
                    temp = root.right
                    if temp.left == None:
                        Minparent = root

                        Min = temp
                        root.val = Min.val
                        if Min.right != None:
                            Minparent.right = Min.right
                        else:
                            Minparent.right = None
                    else:
                        while temp.left != None:
                            Minparent = temp
                            temp = Minparent.left

                        Min = temp
                        root.val = Min.val
                        if Min.right != None:
                            Minparent.left = Min.right
                        else:
                            Minparent.left = None
                            
            self.insert(i,new_val)
                
                
        return i


# 所有參考資料：
# 
# search
# 
# https://www.tutorialspoint.com/python_data_structure/python_binary_search_tree.htm
# 
# delete
# 
# https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
# 
# https://www.twblogs.net/a/5d4e2980bd9eee541c310dd4
# 
# https://www.itread01.com/content/1542339850.html
