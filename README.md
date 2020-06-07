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

```python
from  __future__  import with_statement
from urllib.parse import urlencode
from urllib.request import urlopen
import contextlib
import sys
```  
