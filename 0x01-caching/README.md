<p align="center">
<img src="https://img.shields.io/badge/LINUX-darkgreen.svg"/>
<img src="https://img.shields.io/badge/Shell-ligthgreen.svg"/>
<img src="https://img.shields.io/badge/Vim-green.svg"/>
<img src="https://img.shields.io/badge/Python-blue.svg"/>
<img src="https://img.shields.io/badge/Markdown-black.svg"/><br>	
</p>

---

# 0x01. Caching

This project contains some tasks for learning about the different caching algorithms.

<p align="center">
  <img width="320"  
        src="https://thumbs.gfycat.com/DemandingBeautifulChameleon-max-1mb.gif"
  >
</p>

# Getting Started :running:	
<div style="text-align: justify">

## Table of Contents
* [About](#about)
* [Resources](#resources-books)
* [Requirements](#requirements)
* [Files](#files-file_folder)
* [Tasks](#tasks)
* [Credits](#credits)

## About

- ***[Caching](https://ocw.mit.edu/courses/6-172-performance-engineering-of-software-systems-fall-2018/resources/lecture-14-caching-and-cache-efficient-algorithms/)***

## Resources :books:
Read or watch:
	
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/80px-Google_2015_logo.svg.png)](https://www.google.com/search?q=caching+in+programming&oq=caching+in+pro&aqs=chrome.0.0i512j69i57j0i22i30l8.17562j0j15&sourceid=chrome&ie=UTF-8)

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/70px-Logo_of_YouTube_%282015-2017%29.svg.png)](https://www.youtube.com/results?search_query=caching+in+programming)

- **[Cache replacement policies - FIFO](https://intranet.hbtn.io/rltoken/7jFetr0lWGiaMMhA7iBwuQ)** 
- **[Cache replacement policies - LIFO](https://intranet.hbtn.io/rltoken/xUMuD6y-yKIXDdTvS7hTBg)** 
- **[Cache replacement policies - LRU](https://intranet.hbtn.io/rltoken/Rnwk-rnoyZz6qDrwJGzYfw)** 
- **[Cache replacement policies - MRU](https://intranet.hbtn.io/rltoken/1sSLlFzowTEhU5YM4hmiWg)** 
- **[Cache replacement policies - LFU](https://intranet.hbtn.io/rltoken/Jr1doOF0zxCJBIjg7hSTww)** 

## Requirements
### General

- All files will be interpreted/compiled on *`Ubuntu 18.04 LTS`* using  *` python3 `*  (version 3.7)
- All files should end with a new line
- The first line of all files should be exactly  *` #!/usr/bin/env python3 `* 
- A  *` README.md `*  file, at the root of the folder of the project, is mandatory
- The code should use the  *` pycodestyle `*  style (version 2.5.*)
- All files must be executable
- The length of all files will be tested using  *` wc `* 
- All modules should have a documentation ( *` python3 -c 'print(__import__("my_module").__doc__)' `* )
- All classes should have a documentation *`(python3 -c 'print(__import__("my_module").MyClass.__doc__)')`*
- All functions should have a documentation ( *` python3 -c 'print(__import__("my_module").my_function.__doc__)' `* and python3 -c *` 'print(__import__("my_module").MyClass.my_function.__doc__)' `*)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## More Info

### Parent class BaseCaching
All your classes must inherit from   ` BaseCaching `   defined below:
<details>
  <summary><h4>Click to expand/hide file contents: :floppy_disk:</h4></summary>
  
  ```python
  #!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")

  ```
</details>


### Installation :computer:
	
- Clone this repository: `https://github.com/Alexoat76/holbertonschool-backend.git`	
- Access to directory: `cd 0x01-caching`
- `Compile` accord to `instructions` of each task.

## Files :file_folder:

### Tests :heavy_check_mark:

+ **[tests](./tests)**: Folder of test files. *`Provided by Holberton School`*.
		
---

## Tasks

+ [x] 0\. **Basic dictionary**

+ **[0-basic_cache.py](./0-basic_cache.py)**

Create a class   *` BasicCache `*   that inherits from   *` BaseCaching `*   and is a caching system:
* Use  *` self.cache_data `*  - dictionary from the parent class  *` BaseCaching `* 
* This caching system doesn’t have limit
*  *` def put(self, key, item): `* 
	* Assign to the dictionary  *` self.cache_data `*  the  *` item `*  value for the key  *` key `*.
	* If  *` key `*  or  *` item `*  is  *` None `* , this method should not do anything.
*  *` def get(self, key): `* 
	* Return the value in  *` self.cache_data `*  linked to  *` key `*.
	* If  *` key `*  is  *` None `*  or if the  *` key `*  doesn’t exist in  *` self.cache_data `* , return  *` None `*.

```python3
#!/usr/bin/python3
""" 0-main """
BasicCache = __import__('0-basic_cache').BasicCache

my_cache = BasicCache()
my_cache.print_cache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
print(my_cache.get("D"))
my_cache.print_cache()
my_cache.put("D", "School")
my_cache.put("E", "Battery")
my_cache.put("A", "Street")
my_cache.print_cache()
print(my_cache.get("A"))

```
```bash
$ ./0-main.py
Current cache:
Current cache:
A: Hello
B: World
C: Holberton
Hello
World
Holberton
None
Current cache:
A: Hello
B: World
C: Holberton
Current cache:
A: Street
B: World
C: Holberton
D: School
E: Battery
Street
$ 
```
---

+ [x] 1\. **FIFO caching**

+ **[1-fifo_cache.py](./1-fifo_cache.py)**

Create a class   *` FIFOCache `*   that inherits from   *` BaseCaching `*   and is a caching system:
* Use  *` self.cache_data `*  - dictionary from the parent class  *` BaseCaching `* 
* Can overload  *` def __init__(self): `*  but don’t forget to call the parent init:  *` super().__init__() `* 
*  *` def put(self, key, item): `* 
	* Assign to the dictionary  *` self.cache_data `*  the  *` item `*  value for the key  *` key `*.
	* If  *` key `*  or  *` item `*  is  *` None `* , this method should not do anything.
	* If the number of items in  *` self.cache_data `*  is higher that  *` BaseCaching.MAX_ITEMS `* :
		* Discard the first item put in cache (FIFO algorithm)
		* Print  *` DISCARD: `*  with the  *` key `*  discarded and following by a new line 
*  *` def get(self, key): `*
	* Return the value in  *` self.cache_data `*  linked to  *` key `* .
	* If  *` key `*  is  *` None `*  or if the  *` key `*  doesn’t exist in  *` self.cache_data `* , return  *` None `* .

```python3
#!/usr/bin/python3
""" 1-main """
FIFOCache = __import__('1-fifo_cache').FIFOCache

my_cache = FIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()

```
```bash
$ ./1-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
DISCARD: B
Current cache:
C: Street
D: School
E: Battery
F: Mission
$ 

```
---

+ [x] 2\. **LIFO Caching**

+ **[2-lifo_cache.py](./2-lifo_cache.py)**

Create a class   *` LIFOCache `*   that inherits from  *` BaseCaching `*   and is a caching system:
* Use  *` self.cache_data `*  - dictionary from the parent class  ` BaseCaching ` 
* Can overload  *` def __init__(self): `*  but don’t forget to call the parent init:  *` super().__init__() `* 
*  *` def put(self, key, item): `* 
	* Assign to the dictionary  *` self.cache_data `*  the  *` item `*  value for the key  *` key `*.
	* If  *` key `*  or  *` item `*  is  *` None `*, this method should not do anything.
	* If the number of items in  *` self.cache_data `*  is higher that  *` BaseCaching.MAX_ITEMS `* :
		* Discard the last item put in cache (LIFO algorithm)
		* Print  *` DISCARD: `*  with the  *` key `*  discarded and following by a new line 
*  *` def get(self, key): `* 
	* Return the value in  *` self.cache_data `*  linked to  *` key `* .
	* If  *` key `*  is  *` None `*  or if the  *` key `*  doesn’t exist in  *` self.cache_data `* , return  *` None `* .

```python3
#!/usr/bin/python3
""" 2-main """
LIFOCache = __import__('2-lifo_cache').LIFOCache

my_cache = LIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
```

```bash
$ ./2-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
DISCARD: D
Current cache:
A: Hello
B: World
C: Holberton
E: Battery
Current cache:
A: Hello
B: World
C: Street
E: Battery
DISCARD: C
Current cache:
A: Hello
B: World
E: Battery
F: Mission
DISCARD: F
Current cache:
A: Hello
B: World
E: Battery
G: San Francisco
$ 

```
---

+ [x] 3\. **LRU Caching**

+ **[3-lru_cache.py](./3-lru_cache.py)**

Create a class   *` LRUCache `*   that inherits from   *` BaseCaching `*   and is a caching system:
* Use  *` self.cache_data `*  - dictionary from the parent class  *` BaseCaching `* 
* Can overload  *` def __init__(self): `*  but don’t forget to call the parent init:  *` super().__init__() `* 
*  *` def put(self, key, item): `* 
	* Assign to the dictionary  *` self.cache_data `*  the  *` item `*  value for the key  *` key `* .
	* If  *` key `*  or  *` item `*  is  *` None `* , this method should not do anything.
	* If the number of items in  *` self.cache_data `*  is higher that  *` BaseCaching.MAX_ITEMS `* :
		* Discard the least recently used item (LRU algorithm)
		* Print  *` DISCARD: `*  with the  *` key `*  discarded and following by a new line 
*  *` def get(self, key): `* 
	* Return the value in  *` self.cache_data `*  linked to  *` key `* .
	* If  *` key `*  is  *` None `*  or if the  *` key `*  doesn’t exist in  *` self.cache_data `* , return  *` None `* .

```python3
#!/usr/bin/python3
""" 3-main """
LRUCache = __import__('3-lru_cache').LRUCache

my_cache = LRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()

```
```bash
$ ./3-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
World
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
None
World
Street
DISCARD: D
Current cache:
B: World
C: Street
E: Battery
F: Mission
DISCARD: E
Current cache:
B: World
C: Street
F: Mission
G: San Francisco
DISCARD: B
Current cache:
C: Street
F: Mission
G: San Francisco
H: H
DISCARD: C
Current cache:
F: Mission
G: San Francisco
H: H
I: I
DISCARD: F
Current cache:
G: San Francisco
H: H
I: I
J: J
DISCARD: G
Current cache:
H: H
I: I
J: J
K: K
$ 

```
---

+ [x] 4\. **MRU Caching**

+ **[4-mru_cache.py](./4-mru_cache.py)**

Create a class   *` MRUCache `*   that inherits from   *` BaseCaching `*   and is a caching system:
* Use  *` self.cache_data `*  - dictionary from the parent class  *` BaseCaching `* 
* Can overload  *` def __init__(self): `*  but don’t forget to call the parent init:  *` super().__init__() `* 
*  *` def put(self, key, item): `* 
	* Assign to the dictionary  *` self.cache_data `*  the  *` item `*  value for the key  *` key `* .
	* If  *` key `*  or  *` item `*  is  *` None `* , this method should not do anything.
	* If the number of items in  *` self.cache_data `*  is higher that  *` BaseCaching.MAX_ITEMS `* :
		* Discard the most recently used item (MRU algorithm)
		* Print  *` DISCARD: `*  with the  *` key `*  discarded and following by a new line 
*  *` def get(self, key): `* 
	* Return the value in  *` self.cache_data `*  linked to  *` key `* .
	* If  *` key `* is  *` None `*  or if the  *` key `*  doesn’t exist in  *` self.cache_data `* , return  *` None `* .

```python3
#!/usr/bin/python3
""" 4-main """
MRUCache = __import__('4-mru_cache').MRUCache

my_cache = MRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()
```
```bash
$ ./4-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
World
DISCARD: B
Current cache:
A: Hello
C: Holberton
D: School
E: Battery
Current cache:
A: Hello
C: Street
D: School
E: Battery
Hello
None
Street
DISCARD: C
Current cache:
A: Hello
D: School
E: Battery
F: Mission
DISCARD: F
Current cache:
A: Hello
D: School
E: Battery
G: San Francisco
DISCARD: G
Current cache:
A: Hello
D: School
E: Battery
H: H
DISCARD: H
Current cache:
A: Hello
D: School
E: Battery
I: I
DISCARD: I
Current cache:
A: Hello
D: School
E: Battery
J: J
DISCARD: J
Current cache:
A: Hello
D: School
E: Battery
K: K
$ 

```
---

+ [x] 5\. **LFU Caching**

+ **[100-lfu_cache.py](./100-lfu_cache.py)**

Create a class   *` LFUCache `*   that inherits from   *` BaseCaching `*   and is a caching system:
* Use  *` self.cache_data `*  - dictionary from the parent class  *` BaseCaching `* 
* Can overload  *` def __init__(self): `*  but don’t forget to call the parent init:  *` super().__init__() `* 
*  *` def put(self, key, item): `* 
	* Assign to the dictionary  *` self.cache_data `*  the  *` item `*  value for the key  *` key `* .
	* If  *` key `*  or  *` item `*  is  *` None `* , this method should not do anything.
	* If the number of items in  *` self.cache_data `*  is higher that  *` BaseCaching.MAX_ITEMS `* :
		* Discard the least frequency used item (LFU algorithm)
		* if find more than 1 item to discard, Use the LRU algorithm to discard only the least recently used
		* Print  *` DISCARD: `*  with the  *` key `*  discarded and following by a new line 
*  *` def get(self, key): `*
	* Return the value in  *` self.cache_data `*  linked to  *` key `* .
	* If  *` key `*  is  *` None `*  or if the  *` key `*  doesn’t exist in  *` self.cache_data `* , return  *` None `* .

```python3
#!/usr/bin/python3
""" 100-main """
LFUCache = __import__('100-lfu_cache').LFUCache

my_cache = LFUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
print(my_cache.get("I"))
print(my_cache.get("H"))
print(my_cache.get("I"))
print(my_cache.get("H"))
print(my_cache.get("I"))
print(my_cache.get("H"))
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()
my_cache.put("L", "L")
my_cache.print_cache()
my_cache.put("M", "M")
my_cache.print_cache()
```
```bash
$ ./100-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
World
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
None
World
Street
DISCARD: D
Current cache:
B: World
C: Street
E: Battery
F: Mission
DISCARD: E
Current cache:
B: World
C: Street
F: Mission
G: San Francisco
DISCARD: F
Current cache:
B: World
C: Street
G: San Francisco
H: H
DISCARD: G
Current cache:
B: World
C: Street
H: H
I: I
I
H
I
H
I
H
DISCARD: B
Current cache:
C: Street
H: H
I: I
J: J
DISCARD: J
Current cache:
C: Street
H: H
I: I
K: K
DISCARD: K
Current cache:
C: Street
H: H
I: I
L: L
DISCARD: L
Current cache:
C: Street
H: H
I: I
M: M
$ 

```

---

## Credits

## Author(s):blue_book:

Work is owned and maintained by 
	**`Alex Orland Arévalo Tribaldos`**  and credits for `group projects` are displayed in the respective `README.md` files.

<3915@holbertonstudents.com>
	
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/25px-Octicons-mark-github.svg.png)](https://github.com/Alexoat76)
[![M](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/25px-Twitter_Bird.svg.png)](https://twitter.com/aoarevalot)
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/25px-LinkedIn_logo_initials.png)](https://www.linkedin.com/in/Alexoat76/)

## Acknowledgments :mega: 

### **`Holberton School`** (*providing guidance*)
	
This program was written as part of the curriculum for Holberton School.
Holberton School is a campus-based full-stack software engineering program
that prepares students for careers in the tech industry using project-based
peer learning. For more information,  please visit [this link](https://www.holbertonschool.com/).
![Brand](https://assets.website-files.com/6105315644a26f77912a1ada/610540e8b4cd6969794fe673_Holberton_School_logo-04-04.svg)
