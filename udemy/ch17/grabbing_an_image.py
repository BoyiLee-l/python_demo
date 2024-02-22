import bs4
import requests
# 取得維基百科所有資料
result = requests.get("https://zh.wikipedia.org/zh-tw/%E5%93%88%E5%88%A9%C2%B7%E6%B3%A2%E7%89%B9")
soup = bs4.BeautifulSoup(result.text, "lxml")

image = soup.select("img.mw-file-element")
for i in range(len(image)):
    print(i)
    # print(image[i]["src"])

# 取得指定圖片在第13項
result2 = requests.get("https:" + image[13]['src'])
print(result2.content)

# 將取得資料寫入檔案
# with open("harry_image.jpg", "wb") as f:
#     f.write(result2.content)