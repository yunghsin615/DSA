# Heap Sort
堆積排序法：將一個數列排成完全二元樹，每一個父節點必須大於兩個子節點，形成 Max Heap，將第一個節點與最後一個節點交換，此時最後一個節點為最大的數並以排列完成，忽略最後一個節點重複前面步驟，直至數列排列完成。


# 學習歷程與說明
## 原本的構想：程式碼中的 comparison_1 函式
一開始沒有頭緒，只能先想出如何比較父節點與子節點大小並交換，也就是程式碼中 comparison 的部分，卻忽略了很多細節，於是參考了以下網站，並**自己重寫了一遍**。
   * [參考網站](https://github.com/minsuk-heo/problemsolving/blob/master/sort/HeapSort.py)
   
## 後來更正：程式碼中的 heap_sort 函式
### Part 1 — comparison：先設一個比較的公式
   * array = [ 8, 2, 10, 5, 9, 1, 6, 3, 7, 4 ]
1. 父節點 i 為變數 biggest，left 為左子節點，right 為右子節點。
2. left 小於等於陣列長度減 1（若陣列有 10 個數字，left 只能走到位置 9，因位置從 0 開始），left 的數字大於 i 的數字，此時 left 為變數 biggest（意即左子節點變為最大數）。
3. right 小於等於陣列長度減 1，right 的數字大於 biggest 的數字（意即無論是 i 或是 left 等於 biggest，right 的數字都必須大於他才成立），此時 right 為變數 biggest（意即右子節點變為最大數）。
   * 若 i = 1（數字 2 ），left = 3（數字 5 ），right = 4（數字 9 ）。
   * left 的數字 5 大於 i 的數字 2，此時 left 為 biggest。
   * right 的數字 9 大於 biggest 的數字 5，此時 right 為 biggest。
4. 經過上面兩個 if 判斷式，若 i 已不等於 biggest，則交換 i 與 biggest 的數字（位置並無交換）。
5. 呼叫 comparison 函式，以剛剛的 biggest 為 i，往下檢查所有父節點皆大於子節點。
### Part 2 — heapify：找出最後一個父節點，往前一堆一堆比較。
1. 最後一個父節點為 parent，陣列長度減 2 整除 2。
   * n = 10，最後一個父節點為位置 4（數字 9 ）。
2. 當最後一個父節點大於等於 0（意即位置不能是負數），呼叫 comparison 函式，以 parent 為 i。
3. 比較完畢後，parent 往前順移一位，跑 while 迴圈，直至跑完所有父節點，形成 Max Heap。
### Part 3 — heapsort：將 Max Heap 第一個節點擺至最後，直至排序完成。
1. 先定義 n 為陣列長度。
2. 呼叫 heapify 函式，排出 Max Heap。
3. 設 end 為陣列長度減 1，為最後一個數的位置。
4. 當 end 大於 0（意即陣列至少有兩個數），陣列中位置 0 的數字與 end 的數字交換，此時最後一個位置的數為最大值並且排序完成。
5. 呼叫 comparison 函式，以 0 為 i，以 end 為 n（意即共有 end 個數字要比較）。
   * n = 10，end = 9。
   * 若最大數字 10 已被擺至最後一個位置，代表已排列完成，於是忽略。
   * 由第 1 個數字至第 9 個數字進行 comparison 函式，因此以 end（數字 9 ）為 n。 
6. end 往前順移一位，跑 while 迴圈，直至所有數字皆排序完成。


# 流程圖
![](https://i.imgur.com/pyzzY5Q.jpg)
