import re

text = "from, My number is  0911123123. I am available from 8am to 5pm. fromit"

patt = "from"

nematch = re.search(patt, text)
nematch2 = re.findall(patt, text)
print(nematch.group())
print(nematch.span())
print(nematch.start())
print(nematch.end())
print(nematch2)

text2 = "How are you doing today?"
print(re.findall(r"[a-d]", text2))

text3 = "I have hello, heo, hellllllo, hekko"
print(re.findall(r"he..o", text3))
print(re.findall(r"he[A-Z]*o", text3))
print(re.findall(r"he[A-Z]+o", text3))

text4 = "I say hello06, hello7580"
print(re.findall(r"hello\d{1,3}", text4))

text5 = "My phone number is 08-75555555, and 07-6168743"
print(re.findall(r"0\d-\d{7}", text5))