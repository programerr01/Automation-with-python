#we need bs4 module for this
from bs4 import BeautifulSoup as bs
#also there is requests module required
import requests
#getting name from stdin
name = str(input("enter the name of the article"))

#getting the response for the address
response = requests.get("https://wikipedia.org/wiki/%s" %name)

if response is not None:
    #parsing the response
    html = bs(response.text , 'html.parser')
    #selecting all the paragraph
    paras = html.select("p")
    #storing the input in the file
    with open("%swiki.txt" %name , "a+") as f:
        for para in paras:
            f.write(para.text)
