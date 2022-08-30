<p align="center">
<img src="https://img.shields.io/badge/LINUX-darkgreen.svg"/>
<img src="https://img.shields.io/badge/Shell-ligthgreen.svg"/>
<img src="https://img.shields.io/badge/Vim-green.svg"/>
<img src="https://img.shields.io/badge/Python-blue.svg"/>
<img src="https://img.shields.io/badge/Markdown-black.svg"/><br>	
</p>

---

# 0x02. i18n

This project contains some tasks for learning about how to parametrize Flask templates to display different languages.

<p align="center">
  <img width="320"  
        src="https://www.pistalix.in/wp-content/uploads/2018/11/flask.gif"
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

 - How to parametrize Flask templates to display different languages
 - How to infer the correct locale based on URL parameters, user settings or request headers
 - How to localize timestamps

## Resources :books:
Read or watch:
	
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/80px-Google_2015_logo.svg.png)](https://www.google.com/search?q=parametrize+flask+python&oq=parametrize+Flask&aqs=chrome.1.69i57j33i160l3.2124j0j15&sourceid=chrome&ie=UTF-8)

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/70px-Logo_of_YouTube_%282015-2017%29.svg.png)](https://www.youtube.com/results?search_query=Flask+i18n+tutorial)

- **[Flask-Babel](https://intranet.hbtn.io/rltoken/HAk3v0Rgvbi-116bCRG6cA)** 
- **[Flask i18n tutorial](https://intranet.hbtn.io/rltoken/L6X5jOSYChsvU22J_NrGSw)** 
- **[pytz](https://intranet.hbtn.io/rltoken/U69U_xGwf64mBNvJkWwmsQ)**


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
- All functions and coroutines must be type-annotated.

### Installation :computer:
	
- Clone this repository: `https://github.com/Alexoat76/holbertonschool-backend.git`	
- Access to directory: `cd 0x02-i18n`
- `Compile` accord to `instructions` of each task.

## Files :file_folder:

+ **[templates](./templates)**.
+ **[translations](./translations)**.
		
---

## Tasks

+ [x] 0\. **Basic Flask app**

+ **[0-app.py](./0-app.py)**
+ **[templates/0-index.html](./templates/0-index.html)**

First you will setup a basic Flask app in   *` 0-app.py `*  . Create a single   *` / `*   route and an   *` index.html `*   template that simply outputs “Welcome to Holberton” as page title (  *` <title> `*  ) and “Hello world” as header (  *` <h1> `*  ).
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
