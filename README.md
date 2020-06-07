# WELCOME

 To create an short url using "Tinyurl api" first we have to understand , how we can achieve this.

## STEPS

+ We have to add our url next to the link (<https://tinyurl.com/api-create,php?).>
+ Then we have to access the link and get the response from the api and store it is a variable.
+ Then we read the variable and decode it.
+ We encode the url to make it easily understandable by the browsers.
+ Finally we print the shortened url.

## CODE

### MODULES

First we import necessary modules and libraries

+ We use **__future__** to tell interpreter that this function is compatible with both feature and past versions of python.
+ To _encode_ our url we use **urlencode**
+ To _open_ our url we use **urlopen**
+ To access python _context manager_ we use **contextlib**
+ To access system arguments we use **sys**

```python
from  __future__  import with_statement
from urllib.parse import urlencode
from urllib.request import urlopen
import contextlib
import sys
```
