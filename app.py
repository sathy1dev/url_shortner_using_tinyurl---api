#importing all necessary modules
from __future__ import with_statement
from urllib.parse import urlencode
from urllib.request import urlopen
import contextlib
import sys

#function to create shorturl
def tinyurl(url):
    request_url = ('https://tinyurl.com/api-create.php?' + urlencode({'url': url}))
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')

#THANKS FOR WATCHING, SUBSCRIBE IF YOU LIKE THIS
#COMMENT IF YOU HAVE ANY DOUBTS OR IF YOU WANNA GIVE ME SUGGESTIONS>
#ALL LIVES MATTER (PEACE OUT)

#defining th main function 
def main():
    #storing th e shortened url in a variable 
    for shorturl in map(tinyurl,sys.argv[1:]):
        print(shorturl)



#telling the interpeter to run which function first on starting to run

if __name__ == '__main__':
    main()