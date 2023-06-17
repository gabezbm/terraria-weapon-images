import requests
from bs4 import BeautifulSoup
import regex as re
from os import path

assert path.exists("./assets"), "directory ./assets does not exist"
assert path.getsize("./assets") == 0, "directory ./assets is not empty"

pageResponse = requests.get("https://terraria.fandom.com/wiki/Weapons")
assert pageResponse.status_code == 200, f"response status code: {pageResponse.status_code}"

soup = BeautifulSoup(pageResponse.text, "html.parser")
print(f"crawling from: {soup.title.text}")

imgs = soup.select("div.itemlist ul li span.i a img")
numImgs = len(imgs)
print(f"number of images: {numImgs}")

for i, img in enumerate(imgs):
    imgName = re.sub(r"\s+", "_", img["data-image-name"])
    imgPath = "./assets/" + imgName
    with open(imgPath, "wb") as f:
        f.write(requests.get(img["data-src"]).content)
        print(f"{i / numImgs:.2%} image saved to: {imgPath}", end=" " * 20 + "\r")