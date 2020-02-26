import urllib.request
import re

url = 'https://levproperties.co.uk/'

req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
respData = resp.read()


test = [
    {"input":"<img    title=\"ttl\" src=\"url\" >",
     "output":[
         {
             "url": "url",
             "title": "ttl"
         },
     ]},
    {"input":"<imgt src=\"url1dfdfdfd\"  dfdfd dfdf title=\"title2\"",
         "output":[
         ]
         },
    {"input": "<img src=\"url\"  dfdfd dfdf title=\"title\"> <img src=\"xxx\" title=\"yyy\">",
     "output": [
         {
             "url": "url",
             "title": "title"
         },
         {
             "url": "xxx",
             "title": "yyy"
         }
     ]
     },
    {"input": "<img src=\"url\" title=\"title\"> <img src=\"xxx\" title=\"yyy\">",
     "output": [
         {
             "url": "url",
             "title": "title"
         },
         {
             "url": "xxx",
             "title": "yyy"
         }
     ]
     }
]
        
def link_dictionary(lev_web_page):
    img_links_and_alt = re.findall(r'<img\s+.*',str(lev_web_page))
    print(img_links_and_alt)
    link_dics = []
    for i in img_links_and_alt:
        dict_format = {"url":i[0],"title":i[1]}
        link_dics.append(dict_format)
    return link_dics

link_dictionary("<img    title=\"ttl\" src=\"url\" >")

#link_dictionary(respData)
#for i in link_dictionary(respData):
 #   print(i["url"])
  #  print(i["title"])


# for i in test:
#     input = link_dictionary(i["input"])
#     print(input)
#     print(i["output"])
#     index=0
#     if len(input)==len(i["output"]):
#         for j in input:
#             if ("url"or"title") in j and ("url" or "title") in i["output"][index] and j["url"] == i["output"][index]["url"] and j["title"]==i["output"][index]["title"]:
#                 print("success")
#                 index =index + 1
#             else:
#                 print("values dont match")
#     else:
#         print("the lenth of the lists doesn't match")

