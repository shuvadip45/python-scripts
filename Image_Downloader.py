

#A script to download instagram images
#Enter the image url mannually when prompted and the image would be downloaded


from bs4 import BeautifulSoup
import requests
import datetime


image_url=input("Enter URL: ")
r=requests.get(image_url)
c=r.content
soup=BeautifulSoup(c,"html.parser")
attributes=soup.find("meta" ,{"property":"og:image"}).attrs
download_url=attributes["content"]

dn=requests.get(download_url)

filename= "IMG"+str(datetime.datetime.now())+".jpg"

with open("./"+filename, "wb") as f:
	f.write(dn.content)

print("File downloaded. The file name is: "+filename)
