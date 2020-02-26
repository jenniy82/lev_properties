import urllib.request
import re

url = 'https://levproperties.co.uk/'

req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
respData = resp.read()



def value_from_splitted_string(splitted_string, expression_I_am_looking_for):
    here_your_string = ""
    what_I_am_looking_for = []
    list_of_what_I_am_looking_for = [j for j in splitted_string if expression_I_am_looking_for in j]
    # print("this is what I am looking for: ")
    print(list_of_what_I_am_looking_for)
    if len(list_of_what_I_am_looking_for) != 0:
        what_I_am_looking_for = re.findall(r''+expression_I_am_looking_for+'"(.*)"',list_of_what_I_am_looking_for[0])
    if len(what_I_am_looking_for) != 0:
        here_your_string=what_I_am_looking_for[0]
    return here_your_string


def dict_format(url,title):
    dict_format={}
    if url == "" and title!="":
        dict_format = {}
    elif title == "" and url!="":
        dict_format = {}
    elif title == "" and url == "":
        dict_format={}
    else:
        dict_format= {"url":url,"title":title}
    return dict_format

def get_value_from_list(list):
    value=""
    if len(list)!=0:
        value = list[0]
    return value



test = [
    {"input":"<img    title=\"ttl\" src=\"url\" >",
     "output":[
         {
             "url": "url",
             "title": "ttl"
         },
     ]},
    {"input":"<img   xxx=\"src=\" >",
     "output":[
     ]},
    {"input":"<img   src=\"url\" >",
     "output":[
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
    img_links_and_alt = re.findall(r'<img\s+.*?>',str(lev_web_page))
    link_dics_input = []
    for i in img_links_and_alt:
        split_array = i.split()
        # src_list = [j for j in split_array if "src=" in j]
        # url = re.findall(r'src="(.*)"',src_list[0])
        # title_list = [j for j in split_array if "title=" in j]
        # print("this is title_list: ",title_list)
        # title = re.findall(r'title="(.*)"',title_list[0])
        # print("This is title: ",title)
        url1 = value_from_splitted_string(split_array,"src=")
        print(url1)
        title1 = value_from_splitted_string(split_array,"title=")
        print(title1)
        # dict_format = {"url":url[0],"title":title[0]}
        dictionary = dict_format(url1,title1)
        if dictionary:
            link_dics_input.append(dictionary)
        print("this is link_dics: ")
        print(link_dics_input)
    return link_dics_input


# print(link_dictionary("<img    title=\"ttl\" src=\"url\" >"))

# link_dictionary("<img    title=\"ttl\" src=\"url\" >")

# example_split_string = "<img    title=\"ttl\" src=\"url\" >"
# example_split_array = example_split_string.split()
# print(example_split_array)
# src_list = [i for i in example_split_array if "src=" in i]
# title_list = [i for i in example_split_array if "title=" in i]
#
#
# print(src_list)
# for i in src_list:
#     url = re.findall(r'src=(.*)',i)
#
# print(url)
#
# for i in title_list:
#     title = re.findall(r'title=(.*)',i)
#
# print(title)



#link_dictionary(respData)
#for i in link_dictionary(respData):
#   print(i["url"])
#  print(i["title"])


for i in test:
    input = link_dictionary(i["input"])
    print("This is input:")
    print(input)
    print("This is output:")
    print(i["output"])
    index=0
    if len(input)==len(i["output"]) == 0:
        print("The input and the output are empty")
        continue
    if len(input)==len(i["output"]):
        print(len(input),len(i["output"]))
        for j in input:
            if ("url"or"title") in j and ("url" or "title") in i["output"][index] and j["url"] == i["output"][index]["url"] and j["title"]==i["output"][index]["title"]:
                print("success")
                index =index + 1
            else:
                print("values dont match")
    else:
        print("the lenth of the lists doesn't match")



# def find_expression(expression):
#     expression_list = [j for j in split_array if expression in j]
#     return expression_list

