import requests
import csv
import json

username="akimasa_l"

def gettime(EndTime):
    return EndTime.split("T")[0].replace("-","/")

url=f"https://atcoder.jp/users/{username}/history/json"

r=requests.get(url)
j=json.loads(r.text)

d=dict()
for i in j:
    endtime=gettime(i["EndTime"])
    rating=i["NewRating"]
    d[endtime]=rating

with open("data_t.csv",encoding="utf-8")as f:
    l=list(csv.reader(f))

l.append([0 for i in l[0]])

for i,j in enumerate(l[0]):
    if j in d:
        l[2][i]=d[j]
    else:
        l[2][i]=l[2][i-1]

with open("rating.csv",mode="w",encoding="utf-8",newline="")as f:
    writer= csv.writer(f)
    writer.writerows(l)
