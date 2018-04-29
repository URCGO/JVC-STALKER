from bs4 import BeautifulSoup
import requests
import os
print("////////////////////")
print("/// JV STALKER  ///")
print("///////////////////")
print("Cet outil liste les messages")
auteur = input("Pseudo >>>")

 

url = "http://www.jeuxvideo.com/recherche/forums/0-51-0-1-0-1-0-blabla-18-25-ans.htm?search_in_forum=" + str(auteur) + "&type_search_in_forum=texte_message"
page = requests.get(url)
contents = page.content
soup = BeautifulSoup(contents, 'html.parser')
postList = soup.findAll("a", { "class" : "lien-jv topic-title" });

print(len(postList))
for i in range(len(postList)):
	print("["+auteur+"] : " + postList[i].text)

with open("StalkresultMSG.txt", "w") as text_file:
    print("Result : {}".format(postList), file=text_file)