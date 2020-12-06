# Created by Leon Hunter at 9:54 AM 10/23/2020
# Modified by : Jesh Amera 03/12/2020
#
class Calculator(object):
    def add(self, a, b):
        sum =(a + b)
        return sum # return sum

    def subtract(self, a, b):
        difference = (a - b)
        return difference # return difference

    def multiply(self, a, b):
        product = (a * b)
        return product # return product

    def divide(self, a, b):
        # if (b == 0):
        #     print("invalid, zero division")
        # else:
        quotient = round((a / b), 3)
        return quotient # return quotient

