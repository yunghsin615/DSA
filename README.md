# My Learning Note

 ```
 資料結構與演算法
 巨資三B 金元萱
 ```

## week 1

   中秋節放假

## week 2 

**Linked list & Array**

   Linked list由節點（node）組成資料，再由poiner指向下一個節點，藉此串連起來，因可利用記憶體中零散空間，需要多少就使用多少；有別於Array，已連續資料型態儲存在記憶體中，容易浪費空間。

## week 3

**Stack & Queue**

- Stack：資料以堆疊的方式呈現（疊盤子），先進後出，例子：undo，回上一頁。
   * Push：放資料進Stack
   * Pop：將最上面資料移除
   * Top：讀取最上面資料
   * IsEmpty：確認Stack裡是否有資料
   * getSize：回傳羅馬資料個數

- Queue：資料以排列方式呈現（排隊），先進先出，例子：CPU、印表機，一次照順序執行一個需求。
   * Push：放資料進Queue
   * Pop：將最前面資料移除，又稱Dequeue
   * getFront：讀取第一筆資料
   * getBack：讀取最後一筆資料
   * IsEmpty：確認Queue裡是否有資料
   * getSize：回傳資料個數

## week 4

**Set Mismatch**

- 題目：一個list為[1,2,3,3,3,5]，排出缺失值與重複值。
- 構想：先設一個holder=[0,0,0,0,0,0]，其位置i分別為0,1,2,3,4,5，將list依序填入holder，holder中list[i＝0]-1為0＝holder[0]=list[0]=1，依序檢驗，重複值為3，缺失值為holder.index(0)+1=4。

**Leetcode | Roman to Integer**

- 題目：指定數字為羅馬符號，依照題目給的符號跑出對應數字。
- 構想：先將羅馬符號指定為對應數字{'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}，設定i位置從0至符號個數-1，以符號第i位小於或大於i+1位做判別。 


**Insertion Sort**

- Insertion Sort：將資料以左至右依序檢視，由第一筆開始插入以排序好之資料，插入時以右至左檢視資料。
> `6` 5 3 1 8 7 2 -> 6 `5` 3 1 8 7 2 -> 5 6 `3` 1 8 7 2 -> 3 5 6 `1` 8 7 2 以此類推 
- bubble sort：一次比對、交換一項
- insertion sort：全部比對完才進行交換
- quick sort：在數列中找中間值，分成兩堆比較大小交換位子
-   n*1/2**x＝1 -> log2n=x
