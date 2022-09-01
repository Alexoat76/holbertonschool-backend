<p align="center">
<img src="https://img.shields.io/badge/LINUX-darkgreen.svg"/>
<img src="https://img.shields.io/badge/Shell-ligthgreen.svg"/>
<img src="https://img.shields.io/badge/Vim-green.svg"/>
<img src="https://img.shields.io/badge/Python-blue.svg"/>
<img src="https://img.shields.io/badge/Markdown-black.svg"/><br>	
</p>

---

# 0x02. i18n

This project contains some tasks for learning about how to parametrize **` Flask `** templates to display different languages.

<p align="center">
  <img width="280"  
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
 - How to infer the correct locale based on **` URL parameters `**, user settings or request headers
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
+ **[templates/0-index.html](./templates/0-index.html)**<br>
First you will setup a basic Flask app in   *` 0-app.py `*  . Create a single   *` / `*   route and an   *` index.html `*   template that simply outputs “Welcome to Holberton” as page title (  *` <title> `*  ) and “Hello world” as header (  *` <h1> `*  ).

---

+ [x] 1\. **Basic Babel setup**
+ **[1-app.py](./1-app.py)**
+ **[templates/1-index.html](./templates/1-index.html)**<br>
Install the Babel Flask extension:

```bash
$ pip3 install flask_babel
```
Then instantiate the *` Babel `* object in your app. Store it in a module-level variable named *` babel `*.

In order to configure available languages in our app, you will create a  *` Config `*  class that has a  *` LANGUAGES `*  class attribute equal to  *` ["en", "fr"] `* 

Use *` Config `* to set Babel’s default locale (  *` "en" `*  ) and timezone (  *` "UTC" `*  ).

Use that class as config for your Flask app.

---

+ [x] 2\. **Get locale from request**
+ **[2-app.py](./2-app.py)**
+ **[templates/2-index.html](./templates/2-index.html)**<br>

Create a  *` get_locale `*  function with the  *` babel.localeselector `*  decorator. Use  *` request.accept_languages `*  to determine the best match with our supported languages.

---

+ [x] 3\. **Parametrize templates**
+ **[babel.cfg](./babel.cfg)**
+ **[3-app.py](./3-app.py)**
+ **[templates/3-index.html](./templates/3-index.html)**
+ **[translations/en/LC_MESSAGES/messages.po](./translations/en/LC_MESSAGES/messages.po)**
+ **[translations/fr/LC_MESSAGES/messages.po](./translations/fr/LC_MESSAGES/messages.po)**
+ **[translations/en/LC_MESSAGES/messages.mo](./translations/en/LC_MESSAGES/messages.mo)**
+ **[translations/fr/LC_MESSAGES/messages.mo](./translations/fr/LC_MESSAGES/messages.mo)**<br>

Use the   *` _ `*   or   *` gettext `*   function to parametrize your templates. Use the message IDs   *` home_title `*   and   *` home_header `*  .
Create a   *` babel.cfg `*   file containing

```python3
[python: **.py]
[jinja2: **/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
```
Then initialize your translations with

```bash
$ pybabel extract -F babel.cfg -o messages.pot .
```

and your two dictionaries with

```bash
$ pybabel init -i messages.pot -d translations -l en
$ pybabel init -i messages.pot -d translations -l fr

```
Then edit files  *` translations/[en|fr]/LC_MESSAGES/messages.po `*  to provide the correct value for each message *` ID `* for each language. Use the following translations:

msgid | English | French
------|---------|--------
` home_title ` | ` "Welcome to Holberton" ` | ` "Bienvenue chez Holberton" `  
` home_header ` | ` "Hello world!" ` | ` "Bonjour monde!" ` 

Then compile your dictionaries with
```bash
$ pybabel compile -d translations
```

Reload the home page of your app and make sure that the correct messages show up.

---

+ [x] 4\. **Force locale with URL parameter**
+ **[4-app.py](./4-app.py)**
+ **[templates/4-index.html](./templates/4-index.html)**<br>

In this task, you will implement a way to force a particular locale by passing the   *` locale=fr `*   parameter to your app’s URLs.

In your   *` get_locale `*   function, detect if the incoming request contains   *` locale `*   argument and ifs value is a supported locale, return it. If not or if the parameter is not present, resort to the previous default behavior.

Now you should be able to test different translations by visiting   *` http://127.0.0.1:5000?locale=[fr|en] `*.

Visiting  ***` http://127.0.0.1:5000/?locale=fr `*** 

---

+ [x] 5\. **Mock logging in**
+ **[5-app.py](./5-app.py)**
+ **[templates/5-index.html](./templates/5-index.html)**<br>

Creating a user login system is outside the scope of this project. To emulate a similar behavior, copy the following user table in   *` 5-app.py `*.

```bash
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
```
This will mock a database user table. Logging in will be mocked by passing   *` login_as `*   URL parameter containing the user ID to log in as.

Define a   *` get_user `*  function that returns a user dictionary or   *` None `*   if the ID cannot be found or if   *` login_as `*  was not passed.

Define a   *` before_request `*   function and use the  *` app.before_request `*   decorator to make it be executed before all other functions.   *` before_request `*   should use   *` get_user `*   to find a user 
if any, and set it as a global on   *` flask.g.user `*.

In your HTML template, if a user is logged in, in a paragraph tag, display a welcome message otherwise display a default message as shown in the table below.

msgid | English | French
------|---------|-------
*` logged_in_as `* | *` "You are logged in as %(username)s." `* | *` "Vous êtes connecté en tant que %(username)s." `*  
*` not_logged_in `* | *` "You are not logged in." `* | *` "Vous n'êtes pas connecté." `*

Visiting  ***` http://127.0.0.1:5000/ `***  in your browser should display this:

**Hello world!** <br>
*You are not logged in.*

Visiting  ***` http://127.0.0.1:5000/?login_as=2 `***  in your browser should display this:

**Hello world!** <br>*You are logged in as Beyonce.*

--- 

+ [x] 6\. **Use user locale**
+ **[6-app.py](./6-app.py)**
+ **[templates/6-index.html](./templates/6-index.html)**<br>

Change your  *` get_locale `*   function to use a user’s preferred local if it is supported.<br>
The order of priority should be

1. Locale from URL parameters
2. Locale from user settings
3. Locale from request header
4. Default locale

Test by logging in as different users

**Bonjour monde!** <br>
*Vous êtes connecté en tant que Spock.*

---

+ [x] 7\. **Infer appropriate time zone**
+ **[7-app.py](./7-app.py)**
+ **[templates/7-index.html](./templates/7-index.html)**<br>

Define a  *` get_timezone `*   function and use the   *` babel.timezoneselector `*   decorator.

The logic should be the same as   *` get_locale `*:
1. Find  ` timezone `  parameter in URL parameters
2. Find time zone from user settings
3. Default to UTC

Before returning a URL-provided or user time zone, you must validate that it is a valid time zone. To that, use  *` pytz.timezone `*   and catch the  *` pytz.exceptions.UnknownTimeZoneError `* 
exception.

---

+ [x] 8\. **Display the current time**
+ **[app.py](./app.py)**
+ **[templates/index.html](./templates/index.html)**
+ **[translations/en/LC_MESSAGES/messages.po](./translations/en/LC_MESSAGES/messages.po)**
+ **[translations/fr/LC_MESSAGES/messages.po](./translations/fr/LC_MESSAGES/messages.po)**<br>

Based on the inferred time zone, display the current time on the home page in the default format. For example:

 ` Jan 21, 2020, 5:55:39 AM `   or   ` 21 janv. 2020 à 05:56:28 `

Use the following translations

msgid | English | French 
------|---------|-------
*` current_time_is `* | *` "The current time is %(current_time)s." `* | *` "Nous sommes le %(current_time)s." `* 

Displaying the time in French looks like this:

**Bonjour monde!** <br>
*Vous êtes connecté en tant que Spock.*<br>
*Nous sommes le 1 sept. 2022, 12:12:58.*

Displaying the time in English looks like this:

**Hello world!** <br>
*You are logged in as Beyonce.*<br>
*The current time is Sep 1, 2022, 7:14:56 AM.*

----

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
