"""This is originally a jupyter notebook project to scrape real estate data from
99acres and save them to a ssv for a more organized view. It also crawls through the
urls and finds as much data as it can"""


# coding: utf-8

# In[62]:


import requests
from bs4 import BeautifulSoup


r=requests.get("https://www.99acres.com/residential-apartments-in-bangalore-ffid")

c=r.content

soup=BeautifulSoup(c,"html.parser")

all=soup.find_all("div",{"class":"srpNw_tble"})
all[0].find("span",{"class":"srpNw_price "}).text


# In[69]:


l=[]
base_url="https://www.99acres.com/residential-apartments-in-bangalore-ffid"
for page in range(0,30):
    if page>0:
        url=base_url+"-page-"+str(page+1)
    else:
        url=base_url
    print(url)
    r=requests.get(url)
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    all=soup.find_all("div",{"class":"srpNw_tble"})

    
    for item in all:
        dict={}
        dict["Price"]=item.find("span",{"class":"srpNw_price"}).text.replace("\n","").replace(" ","")
        try:
            dict["Address"]=item.find("a",{"class":"sName"}).text.replace("\n","").replace("\t","")
        except:
            dict["Address"]="None"
        try:
            dict["Bedroom"]=item.find("td",{"class":"_auto_bedroom"}).text.replace("\n","").replace("\t","")
        except:
            dict["Bedroom"]="None"
        try:
            dict["Bathroom"]=item.find("td",{"class":"_auto_bath_balc_roadText"}).text.replace("\n","").replace("\t","")
        except:
            dict["Bathroom"]="None"
        try:
            dict["Square Foot"]=item.find("td",{"class":"_auto_areaValue"}).find("b").text.replace("\n","").replace("\t","")
        except:
            dict["Square Foot"]="None"
        l.append(dict)


# In[70]:


import pandas
df=pandas.DataFrame(l)
df


# In[71]:


df.to_csv("Output.csv")

