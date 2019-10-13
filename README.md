# week 1 

**Linked list & Array**

   Linked list由節點（node）組成資料，再由poiner指向下一個節點，藉此串連起來，因可利用記憶體中零散空間，需要多少就使用多少；有別於Array，已連續資料型態儲存在記憶體中，容易浪費空間。

# week 2

**Stack & Queue**

- Stack：資料以堆疊的方式呈現（疊盤子），先進後出，例子：undo，回上一頁。
   * Push：放資料進Stack
   * Pop：將最上面資料移除
   * Top：讀取最上面資料
   * IsEmpty：確認Stack裡是否有資料
   * getSize：回傳資料個數

- Queue：資料以排列方式呈現（排隊），先進先出，例子：CPU、印表機，一次照順序執行一個需求。
   * Push：放資料進Queue
   * Pop：將最前面資料移除，又稱Dequeue
   * getFront：讀取第一筆資料
   * getBack：讀取最後一筆資料
   * IsEmpty：確認Queue裡是否有資料
   * getSize：回傳資料個數

# week 3

# week 5
- insertion sort
- bubble sort：一次比對、交換一項
- insertion sort：全部比對完才進行交換
- quick sort：在數列中找中間值，分成兩堆比較大小交換位子
-   n*1/2**x＝1 -> log2n=x
