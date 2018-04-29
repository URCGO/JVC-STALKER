from bs4 import BeautifulSoup
import requests
import os
print("////////////////////")
print("/// JV STALKER  ///")
print("///////////////////")
print("Outil de stalk")
print("------------")
print("Voulez vous une liste des topics ou des messages ?")
response=input(">>>")


if response=='topics' in response.lower():
	import topic
elif response=='messages' in response.lower():
	import message
else:
	print('Veuillez entrer "topics" ou "messages"')
	print("Fermeture....")


