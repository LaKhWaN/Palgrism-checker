import requests
from bs4 import BeautifulSoup

search = "Categorical data are values that cannot be measured up against each other" #input("Enter the thing you want to search about on google: ")
Search = search.split()
length = len(Search)
Length = int(length/2)
newSearch_1 = "" # String to search
for i in range(Length):
    newSearch_1+=Search[i]
    newSearch_1+=" "

newSearch = search.replace(" ","+")

url = ("https://www.google.com/search?q="+newSearch)
r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent,'html.parser')
anchors = soup.find_all('a')
f=open("GoogleSearch.txt",'w')
for i in anchors:
    if i['href'][1] == 'u' and i['href'][2] == 'r' and i['href'][3] == 'l' and i['href'][4] == '?':
        f.write("https://www.google.com"+i['href']+"\n")
print("File saved successfully named as GoogleSearch.txt")
f.close()
f=open("GoogleSearch.txt","r")
links = f.readlines()
#print("TOTAL LINKS: ",len(links))
f.close()
f=open("Paras.txt","w")
for link in links: 
    r = requests.get(link)
    htmlContent = r.content

    soup = BeautifulSoup(htmlContent,'html.parser')
    paras = soup.find_all('p')
    try:
        for para in paras:
            f.write(para.getText()+"\n")
            if newSearch_1 in para.getText():
                print(para.getText())
        #print(link)
    except:
        #print("Error")
        pass
f.close()
print("Paras Saved successfully named as Paras.txt")