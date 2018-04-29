from bs4 import BeautifulSoup
import requests

print("////////////////////")
print("/// JV STALKER  ///")
print("///////////////////")
print("Outil de stalk")
auteur = input("Pseudo >>>")



url = "http://www.jeuxvideo.com/recherche/forums/0-51-0-1-0-1-0-blabla-18-25-ans.htm?search_in_forum=" + auteur + "&type_search_in_forum=auteur_topic"
page = requests.get(url)
contents = page.content
soup = BeautifulSoup(contents, 'html.parser')
postList = soup.findAll("topic-title");


for i in range(len(postList)):
	print("["+auteur+"]"+ " : " + postList[i].text)

with open("Stalkresult.txt", "w") as text_file:
    print("Result: {}".format(postList), file=text_file)



    