# ชุดโน้ตบุ๊ก Python: Data Structures and Algorithms

สื่อการสอนสำหรับนิสิต IT ชั้นปีที่ 2 คำอธิบายภาษาไทย + ศัพท์เทคนิคอังกฤษ
อ้างอิงแนวเนื้อหาจาก Narasimha Karumanchi, *Data Structures and Algorithmic Thinking with Python*

## รายการไฟล์

| ไฟล์ | หัวข้อ | สาระสำคัญ |
|---|---|---|
| `01_algorithm_analysis.ipynb` | การวิเคราะห์ประสิทธิภาพ | Big-O / Ω / Θ, การนับ operation, Master Theorem, วัดเวลาจริง |
| `02_arrays_and_recursion.ipynb` | Array และ Recursion | dynamic array ทำเอง, two pointers, sliding window, prefix sum, Kadane, Hanoi |
| `03_linked_list.ipynb` | Linked List | singly / doubly, slow-fast pointer, reverse, cycle detection |
| `04_stack.ipynb` | Stack | 2 แบบ implement, วงเล็บสมดุล, infix→postfix, monotonic stack, min stack |
| `05_queue.ipynb` | Queue / Deque | circular queue, linked queue, queue จาก 2 stacks, sliding window max |
| `06_tree_and_bst.ipynb` | Tree และ BST | traversal 4 แบบ (recursive + iterative), height/diameter, insert/delete BST, LCA |
| `07_heap_priority_queue.ipynb` | Heap | MinHeap ทำเอง, heapq, k largest, merge k lists, streaming median |
| `08_hashing.ipynb` | Hashing | separate chaining, linear probing, rehash, เทียบ hash function, LRU cache |
| `09_graph.ipynb` | Graph | matrix vs list, BFS/DFS, topological sort, Dijkstra, Union-Find + Kruskal |
| `10_sorting.ipynb` | Sorting | 7 อัลกอริทึม + ตารางเปรียบเทียบ, stability, benchmark |
| `11_searching_and_summary.ipynb` | Searching + สรุป | binary search, lower/upper bound, search on answer, ตารางเลือกโครงสร้างข้อมูล |

## วิธีใช้

```bash
pip install notebook       # หรือใช้ JupyterLab / VS Code / Google Colab
jupyter notebook
```

ทุกไฟล์ใช้ **Python standard library เท่านั้น** (ไม่ต้องติดตั้งไลบรารีเพิ่ม) และแต่ละไฟล์รันได้อย่างอิสระตั้งแต่เซลล์แรกถึงเซลล์สุดท้าย

## โครงของแต่ละบท

1. คำอธิบายแนวคิด + ตารางเปรียบเทียบ complexity
2. โค้ด implement จากศูนย์ (พร้อมคอมเมนต์อธิบายทีละบรรทัดสำคัญ)
3. ตัวอย่างการประยุกต์ใช้จริง
4. แบบฝึกหัดท้ายบท 4 ข้อ
5. เฉลยพร้อมโค้ดที่รันได้

## ข้อเสนอแนะการใช้ในชั้นเรียน

- **ก่อนเรียน:** ให้นิสิตอ่านหัวข้อคำอธิบายและรันโค้ดเซลล์แรก ๆ มาก่อน
- **ในคาบ:** ลบ body ของฟังก์ชันสำคัญออก ให้นิสิตเติมเอง (สร้างเป็นไฟล์ `_blank` แยก)
- **การบ้าน:** ใช้แบบฝึกหัดท้ายบท โดยลบเซลล์เฉลยออกก่อนแจก
- **ทดสอบย่อย:** ให้เขียนวิเคราะห์ complexity ของโค้ดในเฉลยเป็นคำตอบอัตนัย

## แหล่งอ้างอิง

- [Karumanchi, *Data Structures and Algorithmic Thinking with Python* (PDF)](https://github.com/Paradorn-248/Computer-Programming/blob/master/Data%20Structure%20and%20Algorithmic%20Thinking%20with%20Python%20%20Data%20Structure%20and%20Algorithmic%20Puzzles%20(%20PDFDrive%20).pdf)
- [Python DSA tutorial — W3Schools](https://www.w3schools.com/python/python_dsa.asp)
- [TimeComplexity — Python Wiki](https://wiki.python.org/moin/TimeComplexity)
- [heapq — Python docs](https://docs.python.org/3/library/heapq.html)
