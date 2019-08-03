
class Calculator:
    def calculate(self):
        self.result = 0
        str(input("Hello this is Eliana, Personal Assistant...\nTry typing \'math\' or \'calculate\' : "))
        self.first_operand = int(input("First Number: "))
        self.operator = input("Operator: ")
        self.second_operand = int(input("Second Number: "))
        if self.operator == "+":
            self.result = self.first_operand + self.second_operand
            print(self.first_operand, "", self.operator, "", self.second_operand, "=", self.result)
        elif self.operator == "-":
            self.result = self.first_operand - self.second_operand
            print(self.first_operand, "", self.operator, "", self.second_operand, "=", self.result)
        elif self.operator == "*":
            self.result = self.first_operand * self.second_operand
            print(self.first_operand, "", self.operator, "", self.second_operand, "=", self.result)
        elif self.operator == "/":
            self.result = self.first_operand / self.second_operand
            print(self.first_operand, "", self.operator, "", self.second_operand, "=", self.result)
        else:
            print("You typed wrong operator: ")
            again()

    def history(self):
        f = open("file.csv", "a+")
        recordhistory = self.first_operand, self.operator, self.second_operand, "=", self.result
        f.write(str(recordhistory))
        f.close()

    def viewHistory(self):
        history = input("Do you want to see calculation history? Y/N \n : ")
        if history.upper() == "Y":
            with open("file.csv", 'r') as viewFileOpen:
                data = viewFileOpen.read()
                #formateddata = data.format(str())
            print("Calculation History: \n", data)
        elif history.upper() == "N":
            print("Thank you!")
        else:
            print("You didn't type Y/N")
            again()
    def clearHistory(self):
        clearhistory = input("Type \"history clear\" if you want to clear the history \n : ")
        if clearhistory.upper() == "HISTORY CLEAR":
            f = open('file.csv', 'r+')
            f.truncate(0)  
            print("History Cleared")
        else:
            print("You didn't type \"history clear\" ")
            again()   

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    # Accept 'y' or 'Y' by adding str.upper()
    if calc_again.upper() == 'Y':
        test = Calculator()
        test.calculate()

    # Accept 'n' or 'N' by adding str.upper()
    elif calc_again.upper() == 'N':
        print('See you later.')

    else:
        again()

def display():
    test = Calculator()
    test.calculate()
    test.history()
    test.viewHistory()
    test.clearHistory()

display()