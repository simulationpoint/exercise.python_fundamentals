# Created by Leon Hunter at 3:57 PM 10/23/2020
# Modified by : Jesh Amera 03/12/2020
#
class StringManipulator(object):
    def get_hello_world(self):
        message = "Hello World"
        return message  # return string

    def concatenate(self, value_to_be_added_to, value_to_add):
        string_concat = (str(value_to_be_added_to) + str(value_to_add))
        return string_concat  # returns concatenated string

    def substring_inclusive(self, string_to_fetch_from, starting_index, ending_index):
        inclusive_op = (string_to_fetch_from[starting_index:ending_index + 1])
        return inclusive_op  # inclusive string manipulation

    def substring_exclusive(self, string_to_fetch_from, starting_index, ending_index):
        exclusive_op = (string_to_fetch_from[starting_index + 1:ending_index])
        return exclusive_op  # exclusive string manipulation

    def compare(self, first_value, second_value):   # compare two strings
        return bool(first_value == second_value)
        # if (first_value == second_value) |
        #    (first_value == False &  second_value == 0) |
        #    (first_value == True &  second_value == 1):
        #     return True
        # else:
        # return False

    def get_middle_character(self, string_to_fetch_from):
        i = [len(string_to_fetch_from) / 2]
        mid_char = string_to_fetch_from[i]
        return mid_char # return the middle character

    def get_first_word(self, string_to_fetch_from):
        return string_to_fetch_from.split()[0] # return the first word

    def get_second_word(self, string_to_fetch_from):
        return string_to_fetch_from.split()[1] # return the second word

    def reverse(self, string_to_be_reversed):
        reverse_string = (string_to_be_reversed[::-1])
        return reverse_string  # return reversed string
