
# coding: utf-8

# # Merge Sort
# 合併排序法：將一個數列不斷對半分成兩個小數列，直至每一個小數列剩下一個元素為止，再將小數列倆倆排序後合併至最後的排序完成數列。

# ## 原本的構想
# ### Part 1 ：將陣列分解
# * 設 array = [ 3, 1, 5, 8, 2, 7, 9, 4 ] 

# 1. 定義 mergesort 函式，若陣列長度小於等於 1 則 return 原陣列，若大於 1 則走完以下步驟。
# 2. 設 mid 為陣列長度一半的位置（也就是數字 8 的位置），mid 以左為 left 陣列，mid 以右為 right 陣列。
# 3. 呼叫 mergesort 函式，重複步驟 2，將 2 個新陣列不斷地對半分至 4 個、8 個新陣列，直至每個新陣列中只剩一個元素（如步驟 1 ）。
# 
# ### Part 2 ：將小陣列倆倆排序合併
# 
# 1. 設 i、j 分別為 left、right 陣列的位置變數，從位置 0 開始。
# 2. 設 for 迴圈，變數 c 代表原陣列的位置 0 至 7 。
# 3. 若 left 陣列中 i 位置的數字小於 right 陣列中 j 位置的數字，i 位置的數字則丟進原陣列的 c 位置，i 位置順移下一位；若 left 陣列中 i 位置的數字大於 right 陣列中 j 位置的數字，j 位置的數字則丟進原陣列的 c 位置，j 位置順移下一位。
#    * 若 left = [ 1, 3, 5, 8 ]，right = [ 2, 4, 7, 9 ]。
#    * c = 0，left [ i = 0 ] 數字 1 小於 right [ j = 0 ] 數字 2，數字 1 丟進原陣列的位置 0，i 移動至 1。
#    * c = 1，left [ i = 1 ] 數字 3 大於 right [ j = 0 ] 數字 2，數字 2 丟進原陣列的位置 1，j 移動至 1。
# 4. 原本認為 c 走完則可將陣列排序完成，但卻出現 error，顯示位置多出 for 迴圈的 range，也就是 i 與 j 會一直順延，即使陣列中已無數字，於是我參考了以下網站，將 for 迴圈改成 while 迴圈。
#    * [參考網站](https://blog.csdn.net/wliu0828/article/details/40426357) 

# In[156]:


def mergesort(array):
    
    if len(array) <= 1: 
        return array   #若陣列中只有一個數字或沒有數字，直接retrun陣列
    
    else:   #若陣列中有兩個以上數字則走以下步驟
        mid = len(array)//2   #mid為陣列長度整除2的位置
        left = array[:mid]   
        right = array[mid:]   #以mid分為左右兩陣列
        
        mergesort(left)   
        mergesort(right)   #呼叫mergesort函式不斷分解左右陣列
        
        i = 0
        j = 0
        
        for c in range(len(array)):   #設變數c為原陣列中的位置
            if left[i] < right[j]:   #若i的數字小於j的數字
                array[c] = left[i]   #i的數字丟進c
                i += 1   
            else:   #若i的數字大於j的數字
                array[c] = right[j]   #j的數字丟進c
                j += 1
    return array


# In[157]:


array=[3,1,5,8,2,7,9,4]
mergesort(array)


# ## 後來更正
# 
# ### Part 1 的步驟無更改 
# ### Part 2 由步驟 3 開始更正
# 1. 設 i、j 分別為 left、right 陣列的位置變數，從位置 0 開始。
# 2. 變數 c 代表原陣列的位置 0 至 7，從位置 0 開始。
# 3. 設 while 迴圈，給予條件式 i 小於 left 陣列長度以及 j 小於 right 陣列長度。若 left 陣列中 i 位置的數字小於 right 陣列中 j 位置的數字，i 位置的數字則丟進原陣列的 c 位置，i 位置順移下一位，c 位置順移下一位；若 left 陣列中 i 位置的數字大於 right 陣列中 j 位置的數字，j 位置的數字則丟進原陣列的 c 位置，j 位置順移下一位，c 位置順移下一位。
#    * 若 left = [ 1, 3, 5, 8 ]，right = [ 2, 4, 7, 9 ]。
#    * c = 0，left [ i = 0 ] 數字 1 小於 right [ j = 0 ] 數字 2，數字 1 丟進原陣列的位置 0，i 移動至 1，c 移動至 1。
#    * c = 1，left [ i = 1 ] 數字 3 大於 right [ j = 0 ] 數字 2，數字 2 丟進原陣列的位置 1，j 移動至 1，c 移動至 2。
# 4. 設第二個 while 迴圈，給予條件式 i 小於 left 陣列長度以及 j 大於等於 right 陣列長度，意即 j 已跑完 right 中所有數字並丟進原陣列，所以將 i 還未跑完的數字依序丟進原陣列，i 與 c 位置順移下一位。
# 5. 設第三個 while 迴圈，給予條件式 i 大於等於 left 陣列長度以及 j 小於 right 陣列長度，意即 i 已跑完 left 中所有數字並丟進原陣列，所以將 j 還未跑完的數字依序丟進原陣列，j 與 c 位置順移下一位。

# #### 註：為何要將 for 迴圈改成 while 迴圈？
# for 迴圈與 while 迴圈的差別在於，for  迴圈以固定數量的數值作為控制條件，如 range ( ) ，while 迴圈以某個條件（條件式）作為控制條件，如 i < len ( left )。以條件式的方式限制 i 與 j 不能超過 left 與 right 陣列的長度，如此就不會有多出來的 index。

# In[167]:


class solution(object):
    def mergesort(self,array):

        if len(array) <= 1: 
            return array   #若陣列中只有一個數字或沒有數字，直接retrun陣列

        else:   #若陣列中有兩個以上數字則走以下步驟
            mid = len(array)//2   #mid為陣列長度整除2的位置
            left = array[:mid]   
            right = array[mid:]   #以mid分為左右兩陣列

            mergesort(left)   
            mergesort(right)   #呼叫mergesort函式不斷分解左右陣列

            i = 0
            j = 0
            c = 0

            while i < len(left) and j < len(right):   #i與j皆小於左右陣列長度
                if left[i] < right[j]:   #若i的數字小於j的數字
                    array[c] = left[i]   #i的數字丟進c
                    i += 1
                else:   #若i的數字大於j的數字
                    array[c] = right[j]   #j的數字丟進c
                    j += 1
                c += 1

            while i < len(left) and j >= len(right):   #j已跑完右陣列的數字
                array[c] = left[i]   #i的數字丟進c
                i += 1
                c += 1

            while i >= len(left) and j < len(right):   #i已跑完右陣列的數字
                array[c] = right[j]   #j的數字丟進c
                j += 1
                c += 1

        return array


# In[168]:


output = solution().mergesort([3,1,5,8,2,7,9,4])
output

