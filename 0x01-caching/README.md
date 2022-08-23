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
  <img width="380"  
        src="https://19yw4b240vb03ws8qm25h366-wpengine.netdna-ssl.com/wp-content/uploads/Everything-You-Need-to-Know-About-API-Pagination-e1639671225295-1024x576.png"
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

- ***[Pagination](https://intranet.hbtn.io/rltoken/WQA53HeWBUH2kAjxVnijfg)***


## Resources :books:
Read or watch:
	
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/80px-Google_2015_logo.svg.png)](https://www.google.com/search?q=caching+in+programming&oq=caching+in+pro&aqs=chrome.0.0i512j69i57j0i22i30l8.17562j0j15&sourceid=chrome&ie=UTF-8)

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/70px-Logo_of_YouTube_%282015-2017%29.svg.png)](https://www.youtube.com/results?search_query=caching+in+programming)

- **[Cache replacement policies - FIFO](https://intranet.hbtn.io/rltoken/7jFetr0lWGiaMMhA7iBwuQ)** 
- **[Cache replacement policies - LIFO](https://intranet.hbtn.io/rltoken/xUMuD6y-yKIXDdTvS7hTBg)** 
- **[Cache replacement policies - LRU](https://intranet.hbtn.io/rltoken/Rnwk-rnoyZz6qDrwJGzYfw)** 
- **[Cache replacement policies - MRU](https://intranet.hbtn.io/rltoken/1sSLlFzowTEhU5YM4hmiWg)** 
- **[Cache replacement policies - LFU](https://intranet.hbtn.io/rltoken/Jr1doOF0zxCJBIjg7hSTww)** 
- What a caching system is
- What FIFO means 
- What LIFO means
- What LRU means
- What MRU means
- What LFU means
- What the purpose of a caching system
- What limits a caching system have

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
  <summary><h3>Click to expand/hide file contents: :floppy_disk:</h3></summary>
  
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

+ [x] 0\. **Simple helper function**

+ **[0-simple_helper_function.py](./0-simple_helper_function.py)**

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
