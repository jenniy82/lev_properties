
from Link_dictionary_parser import Link_dictionary_parser
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
attributes = ["src", "title"]

lev_parser = Link_dictionary_parser(attributes)


for i in test:
    lev_parser.logger.debug("This is i[input]")
    lev_parser.logger.debug(i["input"])
    input = lev_parser.link_dictionary(i["input"])
    lev_parser.logger.debug("This is input:")
    lev_parser.logger.debug(input)
    lev_parser.logger.debug("This is output:")
    lev_parser.logger.debug(i["output"])
    index=0
    if len(input)==len(i["output"]) == 0:
        lev_parser.logger.error("The input and the output are empty")
        continue
    if len(input)==len(i["output"]):
        lev_parser.logger.debug((len(input) , len(i["output"])))
        for j in input:
            if lev_parser.is_attributes_exists_in_dictionary(attributes,j) and lev_parser.is_attributes_exists_in_dictionary(attributes,i["output"][index]):
                lev_parser.logger.debug("The attributes appear in both input and output dictionaries")
            if lev_parser.compare_input_output(attributes,j,i["output"][index]):
                lev_parser.logger.debug("The attributes in input and outpur dictionaries are equal")
                index =index + 1
            else:
                lev_parser.logger.error("values dont match")
    else:
        lev_parser.logger.error("the lenth of the lists doesn't match")
    lev_parser.logger.debug("ALL THE INPUTS AND OUTPUTS ARE EQUAL")