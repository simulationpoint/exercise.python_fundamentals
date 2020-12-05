# Created by Leon Hunter at 3:57 PM 10/23/2020
class StringManipulator(object):
    def get_hello_world(self):
        message = "Welcome to DevOps 2020"
        return message # return string

    def concatenate(self, value_to_be_added_to, value_to_add):
        string_concat = (str(value_to_be_added_to) + str(value_to_add))
        return string_concat # returns concatenated string

    def substring_inclusive(self, string_to_fetch_from, starting_index, ending_index):
        inclusive_op=(string_to_fetch_from [starting_index:ending_index + 1])
        return inclusive_op # inclusive string manipulation

    def substring_exclusive(self, string_to_fetch_from, starting_index, ending_index):
        exclusive_op= (string_to_fetch_from[starting_index + 1:ending_index])
        return exclusive_op # exclusive string manipulation

    def compare(self, first_value, second_value):
        if [(first_value > second_value)]:
            text1 = "first string value is greater"
            return  text1
            else if [(first_value < second_value)]:
                text2 = "first string value is less than the second value"
                return  text2
            else if [(first_value == second_value)]:
            text3="the two values are equal"
            return text3
        else if [(first_value != second_value)]:
        text4=" The two sting values are not equal"
    return text4
        return None # compare two strings

    def get_middle_character(self, string_to_fetch_from):
        return None # TODO - Implement solution

    def get_first_word(self, string_to_fetch_from):
        return None # TODO - Implement solution

    def get_second_word(self, string_to_fetch_from):
        return None # TODO - Implement solution

    def reverse(self, string_to_be_reversed):
        return None # TODO - Implement solution