import re
import logging

class Link_dictionary_parser(object):


    logging.basicConfig(filename="logger.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
    logger=logging.getLogger()
    logger.setLevel(logging.DEBUG)

    def __init__(self,attributes):
        self.attributes = attributes




    def value_from_splitted_string(self,splitted_string, expression_I_am_looking_for):
        here_your_string = ""
        what_I_am_looking_for = []
        list_of_what_I_am_looking_for = [j for j in splitted_string if expression_I_am_looking_for in j]
        # print("this is what I am looking for: ")
        self.logger.debug(f'List of values that I search: {list_of_what_I_am_looking_for}')
        if len(list_of_what_I_am_looking_for) != 0:
            what_I_am_looking_for = re.findall(r'^'+expression_I_am_looking_for+'="(.*)"',list_of_what_I_am_looking_for[0])
        if len(what_I_am_looking_for) != 0:
            here_your_string = what_I_am_looking_for[0]
            self.logger.debug(f'Here is your String: {here_your_string}')
        return here_your_string

    def link_dictionary(self, lev_web_page):
        img_links_and_alt = re.findall(r'<img\s+.*?>',str(lev_web_page))
        link_dics_input = []
        for i in img_links_and_alt:
            attribute_value_list=[]
            split_array = i.split()
            for j in self.attributes:
                attribute_value = self.value_from_splitted_string(split_array,j)
                self.logger.debug(f'[link dictionary] This is attribute value: {attribute_value} ')
                attribute_value_list.append(attribute_value)
            dictionary = self.dict_format(self.attributes,attribute_value_list)
            if dictionary:
                link_dics_input.append(dictionary)
            self.logger.debug("This is link_dics: ")
            self.logger.debug(link_dics_input)
        return link_dics_input



    def is_attributes_exists_in_dictionary(self,list_of_attributes, input_or_output_dictionary):
        exists_in_list = True
        for i in list_of_attributes:
            if i in input_or_output_dictionary:
                exists_in_list
            else:
                self.logger.debug("The attribute "+ i + " doesn't appear in the input dictionary")
                exists_in_list = False
                break
        return exists_in_list

    def compare_input_output(self, attribute_list, input_dictionary, output_dictionary):
        is_equal = True
        for i in attribute_list:
            if input_dictionary[i] == output_dictionary[i]:
                is_equal
            else:
                is_equal = False
                self.logger.debug("The input and output values aren't equal")
        return is_equal


    def is_attributes_exists_in_dictionary(self, list_of_attributes, input_or_output_dictionary):
        exists_in_list = True
        for i in list_of_attributes:
            if i in input_or_output_dictionary:
                exists_in_list
            else:
                self.logger.debug("The attribute "+ i + " doesn't appear in the input dictionary")
                exists_in_list = False
                break
        return exists_in_list

    def compare_input_output(self, attribute_list, input_dictionary, output_dictionary):
        is_equal = True
        for i in attribute_list:
            if input_dictionary[i] == output_dictionary[i]:
                is_equal
            else:
                is_equal = False
                self.logger.debug("The input and output values aren't equal")
        return is_equal

    def dict_format(self,attributes,attribute_value_list):
        dict_format={}
        for i in attribute_value_list:
            if i== "":
                dict_format = {}
                self.logger.warning("this is empty dictionary")
                break
            else:
                dict_format=dict(zip(attributes, attribute_value_list))
                self.logger.debug("This is dict format: ")
                self.logger.debug(dict_format)
        return dict_format

    def get_value_from_list(self,list):
        value=""
        if len(list)!=0:
            value = list[0]
        return value