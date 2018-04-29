from bs4 import BeautifulSoup
import requests
import os
print("////////////////////")
print("/// JV STALKER  ///")
print("///////////////////")
print("Outil de stalk")
auteur = input("Pseudo >>>")

 

url = "http://www.jeuxvideo.com/recherche/forums/0-51-0-1-0-1-0-blabla-18-25-ans.htm?search_in_forum=" + str(auteur) + "&type_search_in_forum=auteur_topic"
page = requests.get(url)
contents = page.content
soup = BeautifulSoup(contents, 'html.parser')
postList = soup.findAll("a", { "class" : "lien-jv topic-title" });

print(len(postList))
for i in range(len(postList)):
	print("["+auteur+"] : " + postList[i].text)
 




