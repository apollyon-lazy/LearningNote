## Demo

### 问题一
假设程序要存储1000个字符串，其中最长的字符串有79个字符，大多数字符串都短得多。此时有两种方案：方案一是全部是字符数组，这样有1000个数组，每个数组有80个字符，共80000个字节，很多内存都未被使用；方案二是创建一个包含1000个指向char的数组，然后使用new根据每个字符串的长度分配响应的内存，这将节省几万个内存。

**:star:要点** 
- 处理字符串(C风格字符串) `strlen(),strcpy(),strcat()`
- 数组存储字符串 `char a[10] = "Hello!";` 
- 指针存储字符串 `char *p = "Hello!";`
- 读取字符串 `cin` `cin.getline(name, Arsize)`  `cin.get(name, Arsize)`  `cin.get()`
- 数组和指针的特殊关系；`*(p + 1) <=> stacks[1]` 
- 动态分配内存 `char *p = new char[strlen(s)+1];` `delete [] p;`

**:memo:程序**
``` C++
  /* save storage */
  const int Arsize = 80;              // enough wide to store string
  char temp[Arsize];                  // temporary storage 
  cin.getline(temp, Arsize);          // get a line input
  char *pn = new char[strlen(temp)+1];// new
  strcpy(pn, temp)                    // copy string into smaller space
  ...                                 // ...
  delete [] pn;                       // delete
```
### 问题二
假设程序要求从文本文件中读取数据，这些信息储存在一个动态分配的结构数组中。每个结构有两个成员，储存姓名的字符数组和浮点型的存款。文本第一行是总人数，下面每一对行中，第一行是姓名，第二行是钱款，文件类似于下面。
``` txt
4
Sam Stone
2000
Freida Flass
10050
Tammy Tubbs
5000
Rich Raptor
8000
```
**:star:要点：** 
- 文件打开 `open(), is_open()`
- 输入对象的基本使用(cin) `inFile >> num; inFile.get()` 
- 文件读取(读取字符串) `inFile.getline(name, Arsize);` `inFile.get(name, Arsize);` `inFile.get();`

**:memo:程序：** 
``` C++
  /* read textfile*/
  ifstream inFile;
  inFile.open(path);
  if (!inFile.is_open())
  {
    cout << "Could not the file" << path << endl;
    exit(EXIT_FAILURE);
  }

  int num;
  inFile >> num;
  inFile.get();
  for (int i = 0; i < num; i++)
  {
    inFile.getline((p + i)->name, Arsize);
    inFile >> (p + i)->money;
    inFile.get();
  }
```