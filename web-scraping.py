from bs4 import BeautifulSoup
import requests

# HTML From File
with open("index.html", "r") as f:
	doc = BeautifulSoup(f, "html.parser")

tags = doc.find_all("p")[0]

print(tags.find_all("b"))

url = "https://www.newegg.ca/hajaan-cyclonia/p/3D5-001V-000T8?Item=9SIARZCJEY8159"

result = requests.get(url)
doc = BeautifulSoup(result.text , "html.parser")

prices = doc.find_all("li",string="$")
print(prices)

