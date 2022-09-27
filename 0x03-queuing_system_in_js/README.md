<p align="center">
<img src="https://img.shields.io/badge/LINUX-darkgreen.svg"/>
<img src="https://img.shields.io/badge/Shell-ligthgreen.svg"/>
<img src="https://img.shields.io/badge/Vim-green.svg"/>
<img src="https://img.shields.io/badge/JavaScript-yellow.svg"/>
<img src="https://img.shields.io/badge/Redis-darkred.svg"/>
<img src="https://img.shields.io/badge/NodeJS-gold.svg"/>
<img src="https://img.shields.io/badge/Express-darkslategray.svg"/>
<img src="https://img.shields.io/badge/Markdown-black.svg"/><br>	
</p>

---

# 0x02. i18n

This project contains some tasks for learning about how to use a Redis client with Node JS for basic and advanced operations. Additionally how to build a basic Express app interacting with a Redis server and queues.

<p align="center">
  <img width="280"  
        src="https://assets.northflank.com/noderedis_bd32becbf1.png"
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

- How to run a Redis server on your machine
- How to run simple operations with the Redis client
- How to use a Redis client with Node JS for basic operations
- How to store hash values in Redis
- How to deal with async operations with Redis
- How to use Kue as a queue system
- How to build a basic Express app interacting with a Redis server
- How to the build a basic Express app interacting with a Redis server and queue

## Resources :books:
Read or watch:
	
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/80px-Google_2015_logo.svg.png)](https://www.google.com/search?q=create+Queues+using+Redis+and+Node.js&oq=create+Queues+using+Redis+and+Node.js&aqs=chrome..69i57j69i59i450l8.265j0j15&sourceid=chrome&ie=UTF-8)

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/70px-Logo_of_YouTube_%282015-2017%29.svg.png)](https://www.youtube.com/results?search_query=+create+Queues+using+Redis+and+Node.js)

- **[Redis quick start](https://intranet.hbtn.io/rltoken/N3VQ8F3JcO_8y2choAxM8A)** 
- **[Redis client interface](https://intranet.hbtn.io/rltoken/LxL6RlhyDI7sytIGk70tJw)** 
- **[Redis client for Node JS](https://intranet.hbtn.io/rltoken/stMk7Lq4xQIvdG_nVGCEgg)** 
- **[` Kue `](https://intranet.hbtn.io/rltoken/YokLsRwYqQrdOAN2hIhkuQ)** 
deprecated but still use in the industry

## Requirements
### General

- All files will be interpreted/compiled on *`Ubuntu 18.04 LTS`* **Node** 12.x, and **Redis** 5.0.7
- All files should end with a new line
- A  *` README.md `*  file, at the root of the folder of the project, is mandatory
- The code should use the *` js `* extension

### Installation :computer:
	
- Clone this repository: `https://github.com/Alexoat76/holbertonschool-backend.git`	
- Access to directory: `cd 0x03-queuing_system_in_js`
- `Compile` accord to `instructions` of each task.

## More Info
## Configuration files
Use these files for the following tasks

<details>
  <summary><h3>package.json :floppy_disk:</h3></summary>

```javascript

{
    "name": "queuing_system_in_js",
    "version": "1.0.0",
    "description": "",
    "main": "index.js",
    "scripts": {
      "lint": "./node_modules/.bin/eslint",
      "check-lint": "lint [0-9]*.js",
      "test": "./node_modules/.bin/mocha --require @babel/register --exit",
      "dev": "nodemon --exec babel-node --presets @babel/preset-env"
    },
    "author": "",
    "license": "ISC",
    "dependencies": {
      "chai-http": "^4.3.0",
      "express": "^4.17.1",
      "kue": "^0.11.6",
      "redis": "^2.8.0"
    },
    "devDependencies": {
      "@babel/cli": "^7.8.0",
      "@babel/core": "^7.8.0",
      "@babel/node": "^7.8.0",
      "@babel/preset-env": "^7.8.2",
      "@babel/register": "^7.8.0",
      "eslint": "^6.4.0",
      "eslint-config-airbnb-base": "^14.0.0",
      "eslint-plugin-import": "^2.18.2",
      "eslint-plugin-jest": "^22.17.0",
      "nodemon": "^2.0.2",
      "chai": "^4.2.0",
      "mocha": "^6.2.2",
      "request": "^2.88.0",
      "sinon": "^7.5.0"
    }
  }

```
</details>

<details>
  <summary><h3>.babelrc.js :floppy_disk:</h3></summary>

```javascript
{
  "presets": [
    "@babel/preset-env"
  ]
}

```
</details>

---

## Tasks

- [x] 0\. **Install a redis instance**
- **[README.md](./README.md)**
- **[dump.rdb](./dump.rdb)**

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
