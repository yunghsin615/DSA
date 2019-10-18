# My Learning Note

 ```
 資料結構與演算法
 巨資三B 金元萱
 ```

## Week 1

中秋節放假  

## Week 2 

**Linked List & Array**

   ![](https://miro.medium.com/max/1732/1*aeJZmbE3xBDZfYOu6p5CPw.png)

- Linked List：由節點（node）組成資料，再由pointer指向下一個節點，藉此串連起來，以null表達終點，可以不連續的資料型態儲存在記憶體中。
   * 優點：可利用記憶體中零散空間，需要多少就使用多少
   * 缺點：無法隨機存取、查詢，需走訪各節點

- Array：以連續的資料型態儲存在記憶體中。
   * 優點：使用容易
   * 缺點：刪除與插入資料較為麻煩、浪費不必要的記憶體空間
   
## Week 3

**Stack & Queue**

![](https://www.thecrazyprogrammer.com/wp-content/uploads/2016/05/Difference-Between-Stack-and-Queue.jpg)

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

## Week 4

**Set Mismatch**

- 題目：一個list為[1,2,3,3,3,5]，排出缺失值與重複值。
- 構想：先設一個holder=[0,0,0,0,0,0]，其位置i分別為0,1,2,3,4,5，將list依序填入holder，holder中list[i＝0]-1為0＝holder[0]=list[0]=1，依序檢驗，重複值為3，缺失值為holder.index(0)+1=4。

**Leetcode | Roman to Integer**

- 題目：指定數字為羅馬符號，依照題目給的符號跑出對應數字。
- 構想：先將羅馬符號指定為對應數字{'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}，設定i位置從0至符號個數-1，以符號第i位小於或大於i+1位做判別。 


**Insertion Sort**

- Insertion Sort：將資料以左至右依序檢視，由第一筆開始插入以排序好之資料，插入時以右至左檢視資料。
> `6` 5 3 1 8 7 2 -> 6 `5` 3 1 8 7 2 -> 5 6 `3` 1 8 7 2 -> 3 5 6 `1` 8 7 2 以此類推 
- bubble sort：將資料由左至右兩兩相互比較、交換位子，最後一位則為已排序好之資料，再從頭開始至全部資料排序結束。
> `6` `5` 3 1 8 7 2 -> 5 `6` `3` 1 8 7 2 -> 5 3 `6` `1` 8 7 2 以此類推
- quick sort：在資料中找基準點，以基準點將資料分為兩堆，在兩堆中繼續找基準點分為四堆，直至排序完成。
   * n*1/2**x＝1 -> log2n=x.
> 6 5 `3` 1 8 7 2 -> 1 2 `3` 6 5 8 7 -> `1` 2 3 6 5 8 `7` -> 1 2 3 6 5 `7` 8 以此類推

## Week 5

國慶日放假


## Week 6

- Heep Sort：將資料轉換為Min/Max Heap結構，以遞增/遞減方式排序，交換最頂層節點與最後一個節點，重複前面步驟直至排序完成。
   * Min Heap：頂層節點數值必定大於下層的二元樹
   * Max Heap：頂層節點數值必定小於下層的二元樹
