import re

with open("gcspartho.txt", "r") as txt:
    string = txt.read()



links = re.findall(r'https://[^\s]+', string)

with open("links.txt", "w") as output:
    for link in links:
        output.write(link+"\n")