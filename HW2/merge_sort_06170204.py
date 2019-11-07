
# coding: utf-8

# 原本的構想：出現 IndexError: list index out of range

# In[13]:


class solution(object):
    def mergesort_1(self,nums):

        if len(nums) <= 1: 
            return nums   #若數列中只有一個數字或沒有數字，直接retrun陣列

        else:   #若陣列中有兩個以上數字則走以下步驟
            mid = len(nums)//2   #mid為陣列長度整除2的位置
            left = nums[:mid]   
            right = nums[mid:]   #以mid分為左右兩陣列

            left = self.mergesort_1(left)   
            right = self.mergesort_1(right)   #呼叫mergesort函式不斷分解左右陣列

            i = 0
            j = 0

            for c in range(len(nums)):   #設變數c為原陣列中的位置
                if left[i] < right[j]:   #若i的數字小於j的數字
                    nums[c] = left[i]   #i的數字丟進c
                    i += 1   
                else:   #若i的數字大於j的數字
                    nums[c] = right[j]   #j的數字丟進c
                    j += 1
        return nums


# In[14]:


output = solution().mergesort_1([3,1,5,8,2,7,9,4])
output


# 後來更正：最終的程式碼

# In[11]:


class solution(object):
    def mergesort(self,nums):

        if len(nums) <= 1: 
            return nums   #若陣列中只有一個數字或沒有數字，直接retrun陣列

        else:   #若陣列中有兩個以上數字則走以下步驟
            mid = len(nums)//2   #mid為陣列長度整除2的位置
            left = nums[:mid]   
            right = nums[mid:]   #以mid分為左右兩陣列

            left = self.mergesort(left)   
            right = self.mergesort(right)   #呼叫mergesort函式不斷分解左右陣列

            i = 0
            j = 0
            c = 0

            while i < len(left) and j < len(right):   #i與j皆小於左右陣列長度
                if left[i] < right[j]:   #若i的數字小於j的數字
                    nums[c] = left[i]   #i的數字丟進c
                    i += 1
                else:   #若i的數字大於j的數字
                    nums[c] = right[j]   #j的數字丟進c
                    j += 1
                c += 1

            while i < len(left) and j >= len(right):   #j已跑完右陣列的數字
                nums[c] = left[i]   #i的數字丟進c
                i += 1
                c += 1

            while i >= len(left) and j < len(right):   #i已跑完右陣列的數字
                nums[c] = right[j]   #j的數字丟進c
                j += 1
                c += 1

        return nums


# In[12]:


output = solution().mergesort([3,1,5,8,2,7,9,4])
output

