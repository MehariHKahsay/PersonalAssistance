
class Calculator:
    print("Hello this is Eliana, Personal Assistant...\n")

    def welcome(self):
        welcomeuser = input("Try typing \'MATH\' or \'CALCULATE\' : ")
        if(welcomeuser.upper() == "MATH") or (welcomeuser.upper() == "CALCULATE"):
            pass
        else:
            #again()
            print("You didn't type \"MATH\" or \"CALCULATE\" :")
            test = Calculator()
            test.welcome()

    def calculate(self):
        self.result = 0
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
            test = Calculator()
            test.calculate()

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
            test = Calculator()
            test.viewHistory()

    def clearHistory(self):
        clearhistory = input("Type \"history clear\" if you want to clear the history \n : ")
        if clearhistory.upper() == "HISTORY CLEAR":
            f = open('file.csv', 'r+')
            f.truncate(0)  
            print("History Cleared")
        else:
            print("You didn't type \"history clear\" ")
            test = Calculator()
            test.clearHistory()   

def display():
    test = Calculator()
    test.welcome()
    test.calculate()
    test.history()
    test.viewHistory()
    test.clearHistory()
     
display()