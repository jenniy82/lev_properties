import urllib.request
import re
import logging

logging.basicConfig(filename="logger.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)


url = 'https://levproperties.co.uk/'

req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
respData = resp.read()

attributes = ["src", "title"]

# first commit

def value_from_splitted_string(splitted_string, expression_I_am_looking_for):
    here_your_string = ""
    what_I_am_looking_for = []
    list_of_what_I_am_looking_for = [j for j in splitted_string if expression_I_am_looking_for in j]
    # print("this is what I am looking for: ")
    logger.debug(f'List of values that I search: {list_of_what_I_am_looking_for}')
    if len(list_of_what_I_am_looking_for) != 0:
        what_I_am_looking_for = re.findall(r'^'+expression_I_am_looking_for+'="(.*)"',list_of_what_I_am_looking_for[0])
    if len(what_I_am_looking_for) != 0:
        here_your_string = what_I_am_looking_for[0]
        logger.debug(f'Here is your String: {here_your_string}')
    return here_your_string


def dict_format(attributes,attribute_value_list):
    dict_format={}
    for i in attribute_value_list:
        if i== "":
            dict_format = {}
            logger.warning("this is empty dictionary")
            break
        else:
            dict_format=dict(zip(attributes, attribute_value_list))
            logger.debug("This is dict format: ")
            logger.debug(dict_format)
    return dict_format

def get_value_from_list(list):
    value=""
    if len(list)!=0:
        value = list[0]
    return value



test = [
    {"input":"<img    title=\"ttl\" src=\"url\"  >",
     "output":[
         {
             "src": "url",
             "title": "ttl",
         },
     ]},
    {"input":"<img    title=\"ttl\" asrc=\"url\" >",
            "output":[
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
             "src": "url",
             "title": "title"
         },
         {
             "src": "xxx",
             "title": "yyy"
         }
     ]
     },
    {"input": "<img src=\"url\" title=\"title\"> <img src=\"xxx\" title=\"yyy\">",
     "output": [
         {
             "src": "url",
             "title": "title"
         },
         {
             "src": "xxx",
             "title": "yyy"
         }
     ]
     }
]

def link_dictionary(lev_web_page):
    img_links_and_alt = re.findall(r'<img\s+.*?>',str(lev_web_page))
    link_dics_input = []
    for i in img_links_and_alt:
        attribute_value_list=[]
        split_array = i.split()
        for j in attributes:
            attribute_value = value_from_splitted_string(split_array,j)
            logger.debug(f'[link dictionary] This is attribute value: {attribute_value} ')
            attribute_value_list.append(attribute_value)
        dictionary = dict_format(attributes,attribute_value_list)
        if dictionary:
            link_dics_input.append(dictionary)
        logger.debug("This is link_dics: ")
        logger.debug(link_dics_input)
    return link_dics_input





for i in test:
    input = link_dictionary(i["input"])
    logger.debug("This is input:")
    logger.debug(input)
    logger.debug("This is output:")
    logger.debug(i["output"])
    index=0
    if len(input)==len(i["output"]) == 0:
        logger.error("The input and the output are empty")
        continue
    if len(input)==len(i["output"]):
        logger.debug((len(input) , len(i["output"])))
        for j in input:
            if ("src"or"title") in j and ("src" or "title") in i["output"][index] and j["src"] == i["output"][index]["src"] and j["title"]==i["output"][index]["title"]:
                logger.debug(" Great success")
                index =index + 1
            else:
                logger.error("values dont match")
    else:
        logger.error("the lenth of the lists doesn't match")



# def find_expression(expression):
#     expression_list = [j for j in split_array if expression in j]
#     return expression_list

