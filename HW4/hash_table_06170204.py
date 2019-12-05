
# coding: utf-8

# In[1]:


from Crypto.Hash import MD5


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def add(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))
        key_code = int(h.hexdigest(),16)
        index = key_code % self.capacity
        new_node = ListNode(key_code)
        
        if self.contains(key) == True:
            return
        else:
            if self.data[index] == None:
                self.data[index] = new_node
            else:
                last = self.data[index]
                
                while last.next != None:
                    last = last.next
                    
                last.next = new_node
        
    def remove(self, key):
        if self.contains(key) != True:
            return
        else:
            h = MD5.new()
            h.update(key.encode("utf-8"))
            key_code = int(h.hexdigest(),16)
            index = key_code % self.capacity
            temp = self.data[index]
            
            if temp.val == key_code:
                if temp.next:
                    self.data[index] = temp.next
                else:
                    self.data[index] = None
            else:
                while temp:
                    if temp.val != key_code:
                        pre = temp
                        temp = temp.next
                    else:
                        break
                        
                if temp.next:
                    pre.next = temp.next
                else:
                    pre.next = None
            

    def contains(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))
        key_code = int(h.hexdigest(),16)
        index = key_code % self.capacity
        temp = self.data[index]
        
        while temp:
            if temp.val != key_code:
                temp = temp.next
            else:
                return True
            
        return False
                


# 所有參考資料：
# https://www.nosuchfield.com/2016/07/29/the-python-implementationp-of-HashTable/
# https://kite.com/python/examples/2084/crypto-generate-a-new-md5-hash
# https://docs.google.com/presentation/d/e/2PACX-1vT1HO9Nl475k2bR0l1x8_Tr4V5Wzx0BEqp9bpmHckvj8kTeJehhYVlOJUDVPhLQm6kjGCJ_sLMSBUw5/pub?start=false&loop=false&delayms=3000&slide=id.p
# https://emn178.pixnet.net/blog/post/93557502
