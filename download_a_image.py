#!/usr/bin/env python3
import urllib.request #import the library

url1 = "https://i.ytimg.com/vi/I0MT8SwNa_U/maxresdefault.jpg"  #url1 is the first variable
url2 = "https://ichef.bbci.co.uk/news/1024/cpsprodpb/184A0/production/_109788499_megan.jpg" #2nd variable
url3 = "https://thoughtcatalog.files.wordpress.com/2018/05/questionstoaskagirl2.jpg"  #3rd variable

urllist= [url1,url2,url3]  # we created list named urllist and the variables
number = 1:  #it should be 1 
for url in urllist:
    urllib.request.urlretrieve(url,"Picture: "+str(number)+".jpg")
    number+=1
