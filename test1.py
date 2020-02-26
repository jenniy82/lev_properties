import re


# def get_value_from_list(list):
#     value=""
#     if len(list)!=0:
#         value = list[0]
#     return value
#
#
# print(get_value_from_list(["gdf","gdfg","d","fg","dfg"]))
# print(get_value_from_list([]))
#
#
#
# def dict_format(url,title):
#     dict_format={}
#     if url == "" and title!="":
#         dict_format = {"title":title}
#     elif title == "" and url!="":
#             dict_format = {"url":url}
#     else:
#         dict_format= {"url":url,"title":title}
#     return dict_format
#
#
#
# print(dict_format("title",""))



def get_value_from_list(splitted_string, expression_I_am_looking_for):
        here_your_string = ""
        list_of_what_I_am_looking_for = [j for j in splitted_string if expression_I_am_looking_for in j]
        print(list_of_what_I_am_looking_for)
        what_I_am_looking_for = re.findall(r''+expression_I_am_looking_for+'"(.*)"',list_of_what_I_am_looking_for[0])
        if len(what_I_am_looking_for) != 0:
            here_your_string=what_I_am_looking_for[0]

        return here_your_string


print(get_value_from_list(["src=\"url\"","test","gdfgdf"],"src="))
