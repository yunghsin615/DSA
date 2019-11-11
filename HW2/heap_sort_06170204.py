
# coding: utf-8

# In[1]:


class Solution(object):
    def heap_sort(self,nums):
        n = len(nums)
        self.heapify(nums,n)   #呼叫heapify函式形成Max Heap
        end = n-1   #最後一個數的位置

        while end > 0:   #陣列至少要有兩個數
            nums[0],nums[end] = nums[end],nums[0]
            self.comparison(nums,0,end)   #呼叫comparison函式由上而下比較
            end -= 1
        return nums

    def comparison(self,nums,i,n):
        biggest = i   #i為biggest
        left = 2*i+1   #left為左子節點
        right = 2*i+2   #right為右子節點

        if left <= n-1 and nums[left] > nums[i]:   #left在陣列長度之內，數字大於i的數字
            biggest = left   #left為biggest

        if right <= n-1 and nums[right] > nums[biggest]:   #right在陣列長度之內，數字大於biggest的數字
            biggest = right   #right為biggest

        if biggest != i:   #若i不為biggest
            nums[i],nums[biggest] = nums[biggest],nums[i]  
            self.comparison(nums,biggest,n)   #重複呼叫函式檢查以下的父節點大於子節點

    def heapify(self,nums,n):
        parent = (n-2)//2   #最後一個父節點

        while parent >= 0:   #位置不能為負數
            self.comparison(nums,parent,n)   #呼叫comparison函式比較
            parent -= 1


# In[2]:


output = Solution().heap_sort([8,2,10,5,9,1,6,3,7,4])
output

