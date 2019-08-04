from inspect import currentframe, getframeinfo

class Calculator:
    print("Hello this is Eliana, Your Personal Assistant...\n")

    def welcome(self):
        welcomeuser = input("Try typing \'MATH\' or \'CALCULATE\' : ")
        if(welcomeuser.upper() == "MATH") or (welcomeuser.upper() == "CALCULATE"):
            pass
        else:
            #again()
            print("You didn't type \"MATH\" or \"CALCULATE\", try again...")
            test = Calculator()
            test.welcome()

    def calculate(self):
        self.result = 0
        try:
            self.first_operand = int(input("First Number: "))
        except :
            print("Not an integer: Try again...")
            self.first_operand = int(input("First Number: "))

        operators = ["+", "-", "*", "/"]
        self.operator = input("Operator: ")

        if self.operator in operators:
            pass
        else:
            print("Wrong operator, try again... ")
            self.operator = input("Operator: ")

        try:
            self.second_operand = int(input("Second Number: "))
        except :
            print("Not an integer: Try again...")
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
            pass

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
            print("History Cleared!")
        else:
            print("You didn't type \"history clear\" ")
            test = Calculator()
            test.clearHistory()   
